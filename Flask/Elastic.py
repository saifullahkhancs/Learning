from http.client import responses
from math import trunc
import logging
from flask import Flask, redirect, url_for , request, render_template , jsonify
from elasticsearch import Elasticsearch
app = Flask(__name__)

# Initilize the Elastic Search CLient
es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
                   basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))

#Define the index name
index_name = 'myindex'

@app.route('/add', methods=['POST'])
def add_data():
    print("tesststs")
    data = request.json  # Get JSON data from the request
    print(data)
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # index the data into the elastic search
    res  = es.index(index=index_name, body=data)
   
    return jsonify(res['result']), 201





#Endpoint to retrieve the data 
@app.route('/search' , methods = ['GET'])
def search_data():
    query = request.args.get('q' , '') # Get search queeryfrom url parameter
    
    if not query: 
        return jsonify({'error': 'No search query provided'}), 400

    #search for th equery in the elasticsearch 
    res = es.search(index= index_name , query = {'match': {'_all' : query} })
    return jsonify(res['hits']['hits;']), 200



if __name__ == '__main__':
    app.run(debug=True)