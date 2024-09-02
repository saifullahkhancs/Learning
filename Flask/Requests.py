import requests
import json
# url of the appllication 
url = 'http://localhost:5000/add'


# Data to be added
data  = {
     'title': 'Elasticsearch Basics',
    'content': 'Learn how to use Elasticsearch with Flask.'
}


responce = requests.post(url=url , json=  data)

# print the responce from the server

print('Status Code:', responce.status_code)
print('Response JSON:',responce.json())



search_url = 'http://localhost:5000/search'


# Query which need to be searched 

query = {  'q' : 'Elasticsearch'}


#Make a get request to get the data 

search_responce = requests.get(search_url , query)

data = search_responce.json()
# total_hits = data['hits']['total']['value']
# print(f"Total Documents Found: {total_hits}")




print('Status Code:', search_responce.status_code)
print('Response JSON:', search_responce.json())
