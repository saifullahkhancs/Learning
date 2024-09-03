from numbers import Real
import requests
import json
# url of the appllication 
add_url = 'http://localhost:5000/add_books'



# Add single data 

data = { 'index' :"books", 
       'document' : { 
           "name": 'Snow Crash' ,
           "author": "Real Stephenson" ,
           "release_date": "1992-06-01",
           "page_count": 470} }

# json_data = json.dumps(data, indent=4)

# responce = requests.post(url=add_url , json=  data)

# print(responce.json())



# Add the Multiple data 

multiple_data = [
        {
            "index": {
                "_index": "books"
            }
        },
        {
            "name": "Revelation Space",
            "author": "Alastair Reynolds",
            "release_date": "2000-03-15",
            "page_count": 585
        },
        {
            "index": {
                "_index": "books"
            }
        },
        {
            "name": "1984",
            "author": "George Orwell",
            "release_date": "1985-06-01",
            "page_count": 328
        },
        {
            "index": {
                "_index": "books"
            }
        },
        {
            "name": "Fahrenheit 451",
            "author": "Ray Bradbury",
            "release_date": "1953-10-15",
            "page_count": 227
        },
        {
            "index": {
                "_index": "books"
            }
        },
        {
            "name": "Brave New World",
            "author": "Aldous Huxley",
            "release_date": "1932-06-01",
            "page_count": 268
        },
        {
            "index": {
                "_index": "books"
            }
        },
        {
            "name": "The Handmaids Tale",
            "author": "Margaret Atwood",
            "release_date": "1985-06-01",
            "page_count": 311
        }
    ]



responce = requests.post(url=add_url , json= multiple_data )

print(responce.json())
