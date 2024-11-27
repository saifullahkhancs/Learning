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
from models import KBCDCPayloadSchema, KBCDCSchema, URL , Domain , IP ,Object
import time
from datetime import datetime
import jmespath



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


async def process_data(data , type ):

    # Intel
    data["_id"] = data["raw"][0].get("id", None)
    data["id"] = data["raw"][0].get("id",None)
    data["srid"] = type + "-" +   data.get("srid" , str(uuid.uuid4()))
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
    data["source"] = jmespath.search("sources[].name", data=data)   # some source repeat soome name appear 2 times?
    logger.info(f"the info {data["source"]} "  )
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
    data["free_verdict"] = data.get("analysis", {}).get("verdict",{})[0].get("value" , None)
    data["free_score"] = data.get("free_score", None)
    data["premium_verdict"] = data.get("premium_verdict", None)
    data["premium_score"] = data.get("premium_score", None)
    data["strike_ready_verdict"] = data.get("verdict", None)
    data["strike_ready_score"] = data.get("score", None)
    data["analyst_score"] = data.get("analyst_score", None ) # int(data.get("analysis", None).get("score",None)[0].get("value" , None))
    data["analyst_updated_at"] = data.get("analyst_updated_at", None)  #
    data["kb_verdict"] = data.get("kb_verdict", None) #
    data["kb_score"] = data.get("kb_score", None) #
    data["malware"] = data.get("malwares", None) 
    data["strike"] = data.get("strikes", None)
    data["tool"] = data.get("tools", None)
    data["cve"] = [data.get("vulnerability", {})[0].get("reported_cves")]
    data["category"]= [data.get("host",{}).get("category", None)]
    # data["threat_actor"] = data.get("threat_actor", None)
    data["threat_actors"] = jmespath.search("threat_actors[*].value" , data =data)
    data["ransom"] = data.get("ransom", None)

    data["targeted_organization"] = jmespath.search("associated_threat_campaigns[*].targeted_organization", data = data)
    data["targets_sector"] = jmespath.search("associated_threat_campaigns[*].targets_sector", None)
    data["targeted_industry"] = jmespath.search("associated_threat_campaigns[*].targeted_industry", data =data) or None
    data["targets_region"] = jmespath.search( "associated_threat_campaigns[*].targets_region", data = data ) or None
    data["targeted_country"] = jmespath.search("associated_threat_campaigns[*].targeted_country", data =data ) or None
    data["attack_origin"] = jmespath.search("associated_threat_campaigns[*].attack_origin", data = data ) or None
    data["whois"] = data.get("whois", None)
    data["tlp"] = [data.get("tlp", None)]




    if type == "url":
        data["ip"] = data.get("ip",None)

    elif type == "domain":
        data["domain"] =[ data.get("host", {}).get("value",None)] #
        data["sr_rank"] =  data.get("sr_rank" , None)#
        data["md5"] = data.get("md5" , None) #
        data["sha1"] = data.get("sha1" , None) #
        data["sha256"]= data.get("sha256" , None) #
        ipv4_list = []
        ips = data.get("infrastructure_info" ,None).get("resolving_ip" , None)
        for ip in ips:
             ipv4 = ip.get("ip" ,None)
             if ipv4:
                ipv4_list.append(ipv4.get("value"))

        data["ipv4"] = ipv4_list
        
        data["email"] = data.get("emails" ,None)

    elif type == "ipv4":
        data["ip"] = data.get("ip" , None)
        data["ip_type"] = data.get("ip_type" , None)
        data["md5"] = data.get("md5" , None) #
        data["sha1"] = data.get("sha1" , None) #
        data["sha256"]= data.get("sha256" , None) 

    elif type =="object":
        data["md5"] = data.get("md5" , None) 
        data["sha1"] = data.get("sha1" , None) 
        data["sha256"]= data.get("sha256" , None)  
        data["sha512"] = data.get("sha512" , None)
        data["node_type"] = data.get("node_type" , None)
        data["size"] = data.get("object_info", {}).get("file_size",None)
        data["file_type"] = [data.get("object_info", {}).get("file_type",None) ]  
        objects =[]
        if data["md5"] is not None:
            objects.append( data["md5"])
        if data["sha1"] is not None:
            objects.append( data["sha1"])
        if data["sha256"] is not None:
            objects.append( data["sha256"])
        if data["sha512"] is not None:
            objects.append( data["sha512"]) 

        data["object"] = objects

    if type in [ "domain" , "url" ,  "ipv4"]:
        data_objects_list = data.get("files_downloaded" , None) # +  data.get("communicating_files" , None)    
        objects = []
        for data_object in data_objects_list:
            object = data_object.get("object",None)
            if object:
                sha1 =  object.get("sha1" ,None)
                if sha1 != None and sha1 != " ":
                            if sha1 not in objects:
                                objects.append(sha1)

                sha256 =  object.get("sha256" ,None)
                if sha256 != None and sha256 != " ":
                            if sha256 not in objects:
                                objects.append(sha256)

                sha512 =  object.get("sha512" ,None)
                if sha512 != None and sha512 != " ":
                            if sha512 not in objects:
                                objects.append(sha512)

                md5 =  object.get("md5" ,None)
                if md5 != None and md5 != " ":
                            if md5 not in objects:
                                objects.append(md5)

        data["object"] = objects

        urls = []
        for source in  data["sources"]:
            url = source.get("url")
            if url:
                urls.append(url)

        # URL Class Properties
        data["url"] = urls if len(urls) > 0 else None

        data["email"] = data.get("emails" ,None)   
        data["domain"] =[ data.get("host", {}).get("value",None)]  # need to solve



    return data 

index_mapper = {
    "url" : "url_data",
    "domain" : "domain_data",
    "ipv4" : "ipv4_data",
    "object" :"object_data"
}


model_mapper = {
    "url" : URL,
    "domain" : Domain,
    "ipv4" : IP,
    "object" :Object
}
consumer = Consumer(config.KAFKA_BOOTSTRAP_SERVERS , loop=loop)
@consumer.consume([config.TOPIC] , group_id=config.KAFKA_INTERNAL_GROUP)
async def process_logs(message: ConsumerRecord):

    try:
        data = message.value
        type = data.get("type")
        pro_data = await process_data(data , type)
        index = index_mapper.get(type)
        model = model_mapper.get(type)
        body = model(**pro_data)
        res = es.index(index=index, id=data.get("_id"),  body=body.dict(exclude_none=True)) 
        # logger.info(f' the responce after saving the data is : - {res} ')
    except Exception as e:
       logger.exception(e)
if __name__ == '__main__':
    loop.run_forever()