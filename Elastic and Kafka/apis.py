import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import uvicorn
from bson import ObjectId
import logging
from models import LogSearch
from elasticsearch import Elasticsearch


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

app  = FastAPI( debug=os.environ.get("DEBUG", "false").lower() == "true")






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
    

# // Remove matching strikes
#       if (ctx._source.containsKey('strike')) {
#         def strikes = ctx._source.strike;
#         def new_strikes = [];
        
#         for (int i = 0; i < strikes.length; i++) {
#           String strike = strikes[i];
#           boolean keep = true;
          
#           // Check if the strike starts with any of the IDs to remove
#           for (int j = 0; j < ids_to_remove.length; j++) {
#             if (strike.startsWith(ids_to_remove[j] + " - ") || 
#                 strike.startsWith(ids_to_remove[j] + ": ")) {
#               keep = false;
#               break;
#             }
#           }
          
#           if (keep) {
#             new_strikes.add(strike);
#           }
#         }
        
#         ctx._source.strike = new_strikes;
#       }



#  "strike_id": [
#             "STA4084",
#             "SMW4047",
#             "SMW4037",
#             "STA4185",
#             "SRV4079",
#             "STA5049",
#             "SMW4184",
#             "SMW4261",
#             "SMW4130"
#           ],




# POST intelligence_kb_artifact*/_update_by_query
# {
#  "script": {
#     "source": """
#       def ids_to_remove =['STA1447', 'STA1473', 'STA1473', 'STA1398', 'SMW1496', 'STA1517', 'SRW1530', 'SMW1531', 'SMW1082', 'STA1377', 'SMW1496: A deep look at Evilnum and its toolset (Copy-1)', 'SMW1496: A deep look at Evilnum and its toolset (Copy-2)', 'SMW1571', 'SRW1580', 'SRE1708 (HTTPS)', 'SRW1692(HTTPS)', 'SRW1675(HTTPS)', 'SRW1707 (HTTPS)', 'SRW1697(HTTPS)', 'SMW1732', 'STA1231', 'SMW1232', 'SMW1445', 'SRV1874', 'STA3087', 'SMW4137', 'STA4139', 'SMW4149', 'SMW4189', 'SMW4249', 'STA4250', 'SMW4270', 'STA4272', 'STA4278', 'SRTS', 'SRTS'];
      
#       def strikes_to_remove = 
#       ['STA1447 - Sofacy Delivers Zebrocy Downloader', 'STA1473 - TESTING APT Attack In the Middle East: The Big Bang', 'STA1473 - (Test1) APT Attack In the Middle East: The Big Bang', 'STA1398 - APT Nazar Delivers Nazar Trojan', 'SMW1496 - Evilnum Malware Attack', 'STA1517 - AgentTesla Targets Spain', 'SRW1530 - HYDRA Ransomware Targets US', 'SMW1531 - SWEED Delivers AgentTesla In Turkey', 'SMW1082 - Mirai Active DDoS malware', 'STA1377 - DoNot Team Delivers Trojan Via MalDoc', 'SMW1496: A deep look at Evilnum and its toolset (Copy-1)', 'SMW1496: A deep look at Evilnum and its toolset (Copy-2)', 'SMW1571 - Unknown Threat Actor Targets UAE Firms By Exploiting Microsoft Exchange Server', 'SRW1580 - Statically Compiled Variants of Linux Based Malware Rekoobe', 'SRE1708 (HTTPS) - Attackers are exploiting zero day RCE flaw to target Windows users', 'SRW1692(HTTPS) - LockBit Ransomware Targets Accenture', 'SRW1675(HTTPS) - AvosLocker enters the ransomware scene asks for partners', 'SRW1707 (HTTPS) - REvil Ransomware Latest Variant ITW', 'SRW1697(HTTPS) - Chaos Ransomware Builder v4 rebranding it as Astra Ransomware', 'SMW1732 - Pakistani Financial Institute Targeted by Unknown Threat Actor old', 'STA1231 - APT34 Delivers TONEDEAF 2.0 To US Companies', 'SMW1232 - CrowdStrike Report 2019 Marked as Malicious', 'SMW1445 - RCtrl Backdoor Delivered By APT30', 'SRV1874 - Unknown Threat Actor Targets Australia With AsyncRAT Followed By Follina Exploitation Testing', 'STA3087 - Unveiling Sea Turtle: Sophisticated Cyber Threats and DNS Hijacking', 'SMW4137 - BlankGrabber Malware Stealing Login Credentials And Sensitive Data', 'STA4139 - Water Curupira Distributing PikaBot Malware Via Phishing', 'SMW4149 - NoaBot Botnet Targeting SSH Servers For Crypto Mining', 'SMW4189 - AceCryptor Packed Rescoms Malware Targets Europe', 'SMW4249 - Fickle Stealer Distributed Via Multiple Attack Chain', 'STA4250 - Naikon Targets Telecoms Operators With Rainyday Malware', 'SMW4270 - Connecio Stealer Delivered Through Fake Falcon Sensor Update Lure', 'STA4272 - MuddyWater Target Middle East With BugSleep', 'STA4278 - APT41 Targets Taiwanese Government Research Institute with ShadowPad', 'SRTS - Benign Strike 01', 'SRTS - Benign Strike 02'];
      
#       if (ctx._source.containsKey('strike_id')) {
#         def strike_ids = ctx._source.strike_id;
#         def updated_strike_ids = [];
        
#         for (int i = 0; i < strike_ids.length; i++) {
#           String id = strike_ids[i];
#           if (!ids_to_remove.contains(id)) {
#             updated_strike_ids.add(id);
#           }
#         }
        
#         ctx._source.strike_id = updated_strike_ids;
#       }
      
#       if (ctx._source.containsKey('strike')) {
#         def strikes = ctx._source.strike;
#         def updated_strikes = [];
        
#         for (int i = 0; i < strikes.length; i++) {
#           String strike = strikes[i];
#           if (!strikes_to_remove.contains(strike)) {
#             updated_strikes.add(strike);
#           }
#         }
        
#         ctx._source.strike = updated_strikes;
#       }
      
#       // Update the count
#       if (ctx._source.containsKey('strike_id')) {
#         ctx._source.strikes_count = ctx._source.strike_id.length;
#       } else {
#         ctx._source.strikes_count = 0;
#       }
#     """
#   },
#  "query": {
#         "match": {
#           "name": "github.com"
#         }
#       }
#   }
  
 