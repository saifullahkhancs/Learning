# import requests 
import asyncio
import json
import asyncio
import uuid
from logger import get_logger
from _kafka import Consumer
from aiokafka import ConsumerRecord
import config
from elasticsearch import Elasticsearch,helpers
from models import KBCDCPayloadSchema, KBCDCSchema, URL
import time
from datetime import datetime
logger = get_logger(__name__ , config.DEBUG)
loop = asyncio.get_event_loop()
es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
                   basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))
try:
    if es.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Failed to connect to Elasticsearch.")
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")


async def process_data(data):

    data["_id"] = data["raw"][0].get("id")
    data["id"] = data["raw"][0].get("id")
    data["srid"] = data.get("srid" , "url" +  str(uuid.uuid4()))
    data["uid"] = str(uuid.uuid4())
    data["name"] = data["value"]
    data["displayName"] = data["value"]
    data["description"] = data.get("description" , None)
    data["type"] = data["type"]
    date =int(time.time())  # int( datetime.fromtimestamp(time.time()))
    data["created_at"] = data.get("created_at",date )
    data["updated_at"] = data.get("updated_at", date)
    data["entity"] = ["url"]
    data["tag"] = data["tags"]
    data["source"] = data["sources"]
    data["strikes_count"] = len(data["strikes"])

    tts = data["mitre_ttp"]
    tactics = []
    techniques = []

    for tactic in tts:
        tactics.append({"mitre_id" : tactic["tac_id"] , "name" : tactic["tac_name"] })
        for tech in tactic["tech"]:
            technique = {"mitre_id" : tech["tech_id"] , "name" : tech["tech_name"] }
            if technique not in techniques:
                techniques.append(technique)

    data["tactic"] = tactics
    data["technique"] = techniques
    data["strike_id"] = data["strikes"]

    # Artifact Class Properties
    data["source_id"] = [data["sources"][0].get("id")] #
    data["alert"] = data.get("alert" , None)
    data["alert_source"] = data.get("alert_source" , None)
    data["case"] = data.get("case" , None)
    data["deployment"] = data.get("deployment" , None)
    data["plan_id"] = data.get("plan_id" , None)
    data["job_id"] =data.get("job_id" , None)
    data["task_id"] = data.get("timestamp" , None)
    data["timestamp"] = data.get("timestamp" , None)
    data["enrichment_user"] = data.get("enrichment_user" , None)
    data["sources_count"] = len(data.get("sources")) if data.get("sources") is not None else None 
    data["alerts_count"] =  len(data.get("alerts")) if data.get("alerts") is not None else None
    data["cases_count"] = len(data.get("case")) if data.get("case") is not None  else None
    data["deployments_count"] = len(data["deployment"]) if data.get("deployment") is not None else None
    data["is_deployable"] = data["artifact_validation"][0].get("is_deployable")
    data["analysis_state"] = data.get("analysis_state" ,None)
    data["community_verdict"] = data.get("community_verdict" ,None)
    data["community_score"] = data.get("community_score" ,None)
    data["free_verdict"] = data.get("analysis", None).get("verdict",None)[0].get("value" , None)
    data["free_score"] = data.get("free_score", None)
    data["premium_verdict"] = data.get("premium_verdict", None)
    data["premium_score"] = data.get("premium_score", None)
    data["strike_ready_verdict"] = data.get("verdict", None)
    data["strike_ready_score"] = data.get("score", None)
    data["analyst_score"] = int(data.get("analysis", None).get("score",None)[0].get("value" , None))
    data["analyst_updated_at"] = data.get("analyst_updated_at", None)  #
    data["kb_verdict"] = data.get("kb_verdict", None) #
    data["kb_score"] = data.get("kb_score", None) #
    data["malware"] = data.get("malwares", None) 
    data["strike"] = data.get("strikes", None)
    data["tool"] = data.get("tools", None)
    data["cve"] = [data.get("vulnerability", None)[0].get("reported_cves")]
    data["category"]= [data.get("host",None).get("category", None)]
    data["threat_actor"] = data.get("threat_actor", None)
    data["threat_actors"] = data.get("threat_actors", None)
    data["ransom"] = data.get("ransom", None)
    data["targeted_organization"] = data.get("associated_threat_campaigns")[0].get("targeted_organization", None)
    data["targets_sector"] = data.get("associated_threat_campaigns")[0].get("targets_sector", None)
    data["targeted_industry"] = data.get("associated_threat_campaigns")[0].get("targeted_industry", None)
    data["targets_region"] = data.get("associated_threat_campaigns")[0].get("targets_region", None)
    data["targeted_country"] = data.get("associated_threat_campaigns")[0].get("targeted_country", None)
    data["attack_origin"] = data.get("associated_threat_campaigns")[0].get("attack_origin", None)
    data["source_type"] = [data["sources"][0].get("type")] #
    data["whois"] = data.get("whois", None)
    data["tlp"] = [data.get("tlp", None)]

    urls = []
    for source in  data["sources"]:
        url = source.get("url")
        if url:
            urls.append(url)
    # URL Class Properties
    data["url"] = urls if len(urls) > 0 else None
    data["object"] = data.get("object" ,None)
    data["email"] = None
    data["domain"] =[ data.get("host",None).get("value",None)]
    data["ip"] = data.get("ip",None)
    return data 
consumer = Consumer(config.KAFKA_BOOTSTRAP_SERVERS , loop=loop)
@consumer.consume([config.TOPIC] , group_id=config.KAFKA_INTERNAL_GROUP)
async def process_logs(message: ConsumerRecord):

    try:
        data = message.value
        pro_data = await process_data(data)
        logger.info(pro_data)
        body = URL(**pro_data)
        
        index = "url_data"
        res = es.index(index=index, body=body.dict(exclude_none=True)) 
        logger.info(f' the responce after saving the data is : - {res} ')
    except Exception as e:
       logger.exception(e)
if __name__ == '__main__':
    loop.run_forever()