from http.client import responses
from math import trunc
import logging
import json

from flask import Flask, redirect, url_for , request, render_template , jsonify
from elasticsearch import Elasticsearch,helpers
from elasticsearch.exceptions import TransportError, ConnectionError, NotFoundError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initilize the Elastic Search CLient
es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http://'}],
                 )

# es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
#                    basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))

try:
    if es.ping():
        logger.info("Connected to Elasticsearch!")
    else:
        raise ConnectionError("Elasticsearch ping returned False")
except Exception as e:
    logger.error(f"Error connecting to Elasticsearch: {e}")
    raise SystemExit(f"Cannot start without Elasticsearch: {e}") from e


@app.route('/<index>')
def start(index):
    try:
        resp = es.search(index=index)
        return jsonify(resp['hits']['hits']), 200
    except NotFoundError:
        return jsonify({"error": f"Index '{index}' not found"}), 404
    except (TransportError, ConnectionError) as e:
        return jsonify({"error": f"Elasticsearch error: {str(e)}"}), 503
    except Exception as e:
        logger.exception(f"Unexpected error searching index '{index}'")
        return jsonify({"error": str(e)}), 500

    
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
    try:
        resp = es.search(
            index='books' , 
            query= {
            'match' : {
                'name' : 'brave'
            }
        }, )
        return jsonify(resp['hits']['hits']), 200
    except NotFoundError:
        return jsonify({"error": "Index 'books' not found"}), 404
    except (TransportError, ConnectionError) as e:
        return jsonify({"error": f"Elasticsearch error: {str(e)}"}), 503
    except Exception as e:
        logger.exception("Error in match endpoint")
        return jsonify({"error": str(e)}), 500



#Define the index name
index_name = 'myindex'

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json  # Get JSON data from the request
 
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # index the data into the elastic search
        res  = es.index(index=index_name, body=data)

        response = es.search(index=index_name, query={"match_all": {}})
        
        # Print out the total number of hits and the documents
        logger.info(f"Total Documents Found: {response['hits']['total']['value']}")
        return jsonify(res['result']), 201
    except (TransportError, ConnectionError) as e:
        return jsonify({"error": f"Elasticsearch error: {str(e)}"}), 503
    except Exception as e:
        logger.exception("Error in add_data endpoint")
        return jsonify({"error": str(e)}), 500








@app.route('/add_books', methods=['POST'])
def add_books():
    try:
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
            res = es.bulk(operations=data)
            return jsonify(res.body);
    except (TransportError, ConnectionError) as e:
        return jsonify({"error": f"Elasticsearch error: {str(e)}"}), 503
    except Exception as e:
        logger.exception("Error in add_books endpoint")
        return jsonify({"error": str(e)}), 500
    





#Endpoint to retrieve the data 
@app.route('/search' , methods = ['GET'])
def search_data():
    query = request.args.get('q' , '') # Get search queeryfrom url parameter
    if not query: 
        return jsonify({'error': 'No search query provided'}), 400

    try:
        res = es.search(index=index_name, query={
        "multi_match": {
            "query": query,  # The search term or query
            "fields": ["title", "content"]  # Fields in which to search
        }
        })
        return jsonify(res['hits']['hits']), 200
    except NotFoundError:
        return jsonify({"error": f"Index '{index_name}' not found"}), 404
    except (TransportError, ConnectionError) as e:
        return jsonify({"error": f"Elasticsearch error: {str(e)}"}), 503
    except Exception as e:
        logger.exception("Error in search_data endpoint")
        return jsonify({"error": str(e)}), 500



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