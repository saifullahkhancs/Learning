from http.client import responses
from math import trunc
import logging
import json

from flask import Flask, redirect, url_for , request, render_template , jsonify
from elasticsearch import Elasticsearch,helpers
from elasticsearch.exceptions import TransportError, ConnectionError
app = Flask(__name__)

# Initilize the Elastic Search CLient
es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http://'}],
                 )

# es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
#                    basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))

try:
    if es.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Failed to connect to Elasticsearch.")
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")


@app.route('/<index>')
def start(index):
    resp = es.search(index=index)
    print(resp['hits']['hits'])

    # The _source of each hit contains the original JSON object 
    # submitted during indexing.

    return jsonify(resp['hits']['hits']), 200

    
@app.route('/delete/<doc_id>', methods=['DELETE'])
def delete_doc(doc_id):
    try:
        # Perform the deletion by document ID
        print(doc_id)
        resp = es.delete(index='intelligence_kb_artifact_object', id=doc_id)
        return jsonify(resp), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route("/indexes")
def get_indexes():
    try:
        # Get a list of all indices in JSON format
        resp = es.cat.indices(format='json')
        
        # Extract index names from the response
        index_names = [index['index'] for index in resp]
        
        # Return the list of index names as JSON response with status code 200
        return jsonify(index_names), 200

    except (TransportError, ConnectionError) as e:
        # Handle any Elasticsearch-related errors
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500


@app.route('/match')
def match():
    resp = es.search(
        index='books' , 
        query= {
        'match' : {
            'name' : 'brave'
        }
    }, )
    print(resp['hits']['hits'])

    return jsonify(resp['hits']['hits']), 200



#Define the index name
index_name = 'myindex'

@app.route('/add', methods=['POST'])
def add_data():
    print("tesststs")
    data = request.json  # Get JSON data from the request
 
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # index the data into the elastic search
    res  = es.index(index=index_name, body=data)
    print(res['result'])

    response = es.search(index=index_name, query={"match_all": {}})
    
    # Print out the total number of hits and the documents
    print(f"Total Documents Found: {response['hits']['total']['value']}")
    for hit in response['hits']['hits']:
        print(f"ID: {hit['_id']}, Source: {hit['_source']}")
    return jsonify(res['result']), 201








@app.route('/add_books', methods=['POST'])
def add_books():

    data =  request.json  # Get JSON data from the request
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    

    if (len(data) == 1):
        # Check if the 'index' key exists and its value is not empty
        index = data.get('index') if data.get('index') else index_name
        
        # Check if 'document' key exists and is neither None nor empty
        if not data.get('document'):
            return jsonify({'error': 'No value provide provided'}), 400


        res = es.index(index=index , body=data['document'])

        return jsonify(res.body);
    else:
        # ndjson_data = "\n".join(json.dumps(op) for op in data) + "\n"
        # res = helpers.bulk(es, data);
        # bulk_data = []
        # for item in data:
        #     op_type = item.pop('_op_type', 'index')  # Default to 'index' if _op_type is not present
        #     index_data = {
        #         op_type: {
        #             "index": item.pop('_index'),
        #             **item
        #         }
        #     }

        # bulk_data = []
        # for item in data:
        #     op_type = item.pop('_op_type', 'index')  # Default to 'index' if _op_type is not present
        #     index_meta = {op_type: {"_index": item.pop('_index')}}
        #     bulk_data.append(index_meta)
        #     bulk_data.append(item['_source'])
            
        res = es.bulk(operations=data)
        return jsonify(res.body);
    





#Endpoint to retrieve the data 
@app.route('/search' , methods = ['GET'])
def search_data():
    query = request.args.get('q' , '') # Get search queeryfrom url parameter
    print(query)
    if not query: 
        return jsonify({'error': 'No search query provided'}), 400

    #search for th equery in the elasticsearch 
    # res = es.search(index= index_name , query = {'match': {'_all' : query} })
    
    # there is the issue with the using of the _all


    res = es.search(index=index_name, query={
    "multi_match": {
        "query": query,  # The search term or query
        "fields": ["title", "content"]  # Fields in which to search
    }
    })
    print(res['hits']['hits'])
    return jsonify(res['hits']['hits']), 200



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
    app.run(debug=True)