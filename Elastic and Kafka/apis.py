from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import uvicorn
from bson import ObjectId
import logging
from models import LogSearch
from elasticsearch import Elasticsearch



es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
                   basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))
try:
    if es.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Failed to connect to Elasticsearch.")
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")

app  = FastAPI( debug=True)






def BuildQuery(start_timestamp, log_level , end_timestamp , message_value):
    must_clauses = []
    if start_timestamp is  not None:
        must_clauses.append( {"range": {
                "timestamp": {
                    "gte": start_timestamp  # Greater than condition
                }
            }
        } )
    if log_level is  not None:
        must_clauses.append(  {
                "match": {
                    "log_level": log_level  # Less than condition
                }
        } )
    if message_value is  not None:
        must_clauses.append( {
                "match": {
                    "message": message_value  # Less than condition
                }
        } ) 
    if end_timestamp is  not None:
        must_clauses.append( {"range": {
                "timestamp": {
                    "lte": end_timestamp  # Less than condition
                }
            }
        } ) 
    return  {
            "bool": {
                "must": must_clauses  # Combine all conditions in must
        }
    }



@app.post("/get_logs")
def  log_search(body : LogSearch ) :
    try:
        query= {}
        index='log_data' , 
        start_timestamp = body.start_timestamp
        log_level  = body.log_level
        end_timestamp = body.end_timestamp
        message_value  = body.message_value

        print(start_timestamp, log_level , end_timestamp , message_value)
        if start_timestamp is None and log_level is None and end_timestamp is None and message_value is None:
            
            query= {
                    "match_all": {}
                }
            
        else:
            query = BuildQuery(start_timestamp, log_level , end_timestamp , message_value)

        print(query)
        resp = es.search(index=index , query= query)
        print(resp['hits']['hits'])
        return JSONResponse(content=resp['hits']['hits'])
    except Exception as e:
        return JSONResponse({"error" : e})



    return JSONResponse(resp['hits']['hits']).body, 200
    






if __name__ == "__main__":
    print("Running FastAPI server...")
    print("Swagger UI available at: http://127.0.0.1:8000/docs")
    print("ReDoc available at: http://127.0.0.1:8000/redoc")

    uvicorn.run("apis:app", host="127.0.0.1", port=8000, reload=True)

    # app.run(host="127.0.0.1", port=8000, reload=True)  
    