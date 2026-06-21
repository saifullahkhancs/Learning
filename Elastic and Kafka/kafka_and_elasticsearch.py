import os

from elasticsearch import Elasticsearch,helpers
from elasticsearch.exceptions import TransportError, ConnectionError, NotFoundError
from http.client import responses
from math import trunc
import logging
import json

from flask import Flask, redirect, url_for , request, render_template , jsonify

ES_HOST = os.environ.get("ES_HOST", "localhost")
ES_PORT = int(os.environ.get("ES_PORT", "9200"))
ES_USER = os.environ.get("ES_USER", "elastic")
ES_PASSWORD = os.environ.get("ES_PASSWORD", "")

es = Elasticsearch([{'host': ES_HOST, 'port': ES_PORT, 'scheme': 'http'}],
                   basic_auth=(ES_USER, ES_PASSWORD))

try:
    if es.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Failed to connect to Elasticsearch.")
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")

app = Flask(__name__)

@app.route('/<index>')
def start(index):
    resp = es.search(index=index)
    print(resp['hits']['hits'])
    return jsonify(resp['hits']['hits']), 200


@app.route("/indexes")
def get_indexes():
    try:
        resp = es.cat.indices(format='json')
        
        index_names = [index['index'] for index in resp]
        
        return jsonify(index_names), 200

    except (TransportError, ConnectionError) as e:
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500



@app.route('/post', methods=['POST'])
def add_books():

    data =  request.json  # Get JSON data from the request
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    index_name  = "intelligence_kb_artifact_object"
    if (len(data) == 1):
        # Check if the 'index' key exists and its value is not empty
        index = data.get('index') if data.get('index') else index_name
        
        # Check if 'document' key exists and is neither None nor empty
        if not data.get('document'):
            return jsonify({'error': 'No value provide provided'}), 400


        res = es.index(index=index , body=data['document'])

        return jsonify(res.body);
    else:
            
        res = es.bulk(operations=data)
        return jsonify(res.body);



@app.route('/update/<index>', methods=['POST'])
def update(index):
    # Define the query to find documents with TLP (case insensitive)
    query = {
        "query": {
            "bool": {
                "should": [
                    {"term": {"tlp": "WHITE"}},
                ]
            }
        }
    }

    # Search for documents matching the query
    search_resp = es.search(index=index, body=query)

    # Prepare bulk update actions
    actions = []
    for doc in search_resp['hits']['hits']:
        doc_id = doc['_id']
        actions.append({
            "update": {
                "_index": index,
                "_id": doc_id,
            }
        })
        actions.append({
            "doc": {
                "tlp": "white"  # Set TLP to lowercase "white"
            }
        })

    # Execute bulk update if there are actions to perform
    if actions:
        es.bulk(body=actions)

    return jsonify({"updated_count": len(actions)}), 200

@app.route('/updatetlp/<index>', methods=['POST'])
def updatetlp(index):
    query = {
    "script": {
         "source": """
      if (ctx._source.tlp.contains('WHITE')) {
        ctx._source.tlp.remove(ctx._source.tlp.indexOf('WHITE'));
        ctx._source.tlp.add('white');
      }
    """,
        "lang": "painless"
    },
      "query": {
    "bool": {
      "must": [
        { "term": { "tlp": "WHITE" } },
        { "exists": { "field": "tlp" } }
      ]
    }
  }
}

    try:
        # Execute the update by query
        response = es.update_by_query(index=index, body=query)
        print(response)
        return jsonify({
            "updated_docs": response["updated"],
            "total_docs": response["total"]
        }), 200  # Return a 200 OK status
        

        return jsonify(response_dict), 200  
        return jsonify(response), 200  # Return the response with a 200 OK status
    
    except NotFoundError:
        return jsonify({"error": "Index not found"}), 404 
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle exceptions with a 500 Internal Server Error


@app.route('/delete_all/<index>', methods=['DELETE'])
def delete_all(index):
    try:
        # Delete all documents in the specified index
        response = es.delete_by_query(index=index, body={
            "query": {
                "match_all": {}
            }
        })
        # Convert the response to a dictionary
        response_dict = {
            "deleted": response['deleted'],
            "took": response['took'],
            "timed_out": response['timed_out'],
            "total": response['total'],
            "failures": response['failures']
        }

        return jsonify(response_dict), 200  

        # return jsonify(response), 200  # Return the response with a 200 OK status
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

if __name__ == '__main__':
    app.run(debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true")