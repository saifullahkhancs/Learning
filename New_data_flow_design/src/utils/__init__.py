
from .concurrency import run_in_threadpool, run_as_async
from models import URL , Domain , IP ,Object
import asyncio
import json
import asyncio
import uuid
from logger import get_logger
import  config
import traceback

import time
from datetime import datetime
import jmespath

logger = get_logger(__name__ , config.DEBUG)

async def process_data(data , artifact_type ):
    try:
    # Intel
        data["_id"] = data["raw"][0].get("id", None)
        data["id"] = data["raw"][0].get("id",None)
        data["srid"] = str(artifact_type + "-" + data.get("srid" , str(uuid.uuid4())))
        data["uid"] = str(uuid.uuid4())
        data["name"] = data["value"]
        data["displayName"] = data["value"]
        data["description"] = data.get("description" , None)
        data["type"] = data["type"]
        date =int(time.time()) 
        data["created_at"] = data.get("created_at",date )
        data["updated_at"] = data.get("updated_at", date)
        data["entity"] = ["url"]
        data["tag"] = data["tags"]
        data["source"] = jmespath.search("sources[].name", data=data) or None   # some source repeat soome name appear 2 times?
        if data["source"] != None:
            data["source"] == list(set(data["source"]))
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
        data["source_id"] =  None
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

        data["free_verdict"] = data.get("free_verdict" , None)
        data["free_score"] = data.get("free_score", None)
        data["premium_verdict"] = data.get("premium_verdict", None)
        data["premium_score"] = data.get("premium_score", None)
        data["strike_ready_verdict"] = data.get("strike_ready_verdict", None)
        data["strike_ready_score"] = data.get("strike_ready_score", None)
        data["analyst_score"] = data.get("analyst_score", None )
        data["analyst_updated_at"] = data.get("analyst_updated_at", None)  
        data["kb_verdict"] = data.get("verdict", None) 
        data["kb_score"] = data.get("score", None) 

        data["malware"] = jmespath.search("malwares[*].value" , data=data) or None 
        data["strike"] = data.get("strikes", None)
        data["tool"] = jmespath.search("tools[*].value" , data=data) or  None
        data["cve"] = jmespath.search("vulnerability[*].reported_cves" , data = data) or None 
        data["category"]= [jmespath.search("host.category" , data= data)]  if jmespath.search("host.category" , data= data) else  None
        data["threat_actor"] = data.get("threat_actor", None)
        data["threat_actors"] = jmespath.search("threat_actors[*].value" , data =data) or None
        print(f" the data in the threrat actor is {data["threat_actors"]} ")
        data["ransom"] = data.get("ransom", None)

        data["targeted_organization"] = jmespath.search("associated_threat_campaigns[*].targeted_organization[]", data = data) or None
        data["targets_sector"] = jmespath.search("associated_threat_campaigns[*].targets_sector[]", None)
        data["targeted_industry"] = jmespath.search("associated_threat_campaigns[*].targeted_industry[]", data =data) or None
        data["targets_region"] = jmespath.search( "associated_threat_campaigns[*].targets_region[]", data = data ) or None
        data["targeted_country"] = jmespath.search("associated_threat_campaigns[*].targeted_country[]", data =data ) or None
        data["attack_origin"] = jmespath.search("associated_threat_campaigns[*].attack_origin[]", data = data ) or None

        data["source_type"] = jmespath.search("sources[*].type" , data=data) or None  # repeatation
        if data["source_type"] != None:
            data["source_type"] = list(set(data["source_type"]))
        data["whois"] = data.get("whois", None)
        data["tlp"] = [data.get("tlp", None)]




        if artifact_type in [ "domain" , "url" ,  "ipv4", "object"]:
            data["email"] = data.get("emails" ,None)   

            domain_list  = []
            ip_list= []
            url_list = []
            domain_list = ([jmespath.search("host.value", data=data)] or []
            if (jmespath.search("host.category", data=data ) or None) == "domain" 
            else [])
            ip_list = ([jmespath.search("host.value", data=data)] or []
            if (jmespath.search("host.category", data=data ) or None) == "ip" 
            else [])
            url_list = ([jmespath.search("host.value", data=data)] or []
            if (jmespath.search("host.category", data=data ) or None) == "url" 
            else [])

            print(f" on line 126 {ip_list}")
            objects =[]
            data["md5"] = data.get("md5" , None) 
            data["sha1"] = data.get("sha1" , None) 
            data["sha256"]= data.get("sha256" , None)  
            data["sha512"] = data.get("sha512" , None)
            

            hashes_list = ["md5","sha1","sha256","sha512"]
            files_downloaded_objects_list = jmespath.search("files_downloaded[*].object[]",data = data) or []       # exist in the domain and url 
            communicating_files_objects_list = jmespath.search("communicating_files[*].object[]",data = data) or []     # exist in the ip 

            # object_list = files_downloaded_objects_list.extend(communicating_files_objects_list)  can not assign this because if when one of the list 
            #                                                                                       is empty it returns None             
            files_downloaded_objects_list.extend(communicating_files_objects_list)
            if files_downloaded_objects_list !=None:
                for data_object in files_downloaded_objects_list:
                        for hash in hashes_list:
                            value  =  data_object.get(hash)
                            if value != None and value != "":
                                    if value not in objects:
                                        objects.append(value)
            # handling the sha's for the object 
            sha1 =  data.get("sha1" ,None)
            if sha1 != None and sha1 != "":
                if sha1 not in objects:
                    objects.append(sha1)

            sha256 =  data.get("sha256" ,None)
            if sha256 != None and sha256 != "":
                if sha256 not in objects:
                    objects.append(sha256)

            sha512 =  data.get("sha512" ,None)
            if sha512 != None and sha512 != "":
                if sha512 not in objects:
                    objects.append(sha512)

            md5 =  data.get("md5" ,None)
            if md5 != None and md5 != " ":
                if md5 not in objects:
                     objects.append(md5)

            data["object"] = objects


            source_url = jmespath.search("sources[*].url" ,data=data) or  []   # this refer to source url 
            for url in source_url:
                    if url not in url_list:
                       url_list.append(url)
            associated_url_from_thread_campagin = jmespath.search("associated_threat_campaigns[].sources[].url" ,data=data) or []
            for url in associated_url_from_thread_campagin:
                if url not in url_list:
                    url_list.append(url)


        if artifact_type == "url":
            ip_value = data.get("ip",None)
            if ip_value and ip_value not in ip_list:
               ip_list.append(ip_value)
            url  = data.get("value" , None)
            if url and url not in url_list:
               url_list.append(url)


        elif artifact_type == "domain":
            data["sr_rank"] =  data.get("sr_rank" , None)
            data["ipv4"] =  jmespath.search("raw[*].*[].details[].ip_address" ,data = data) or None   
            data["email"] = data.get("emails" ,None)
            domain  = data.get("value")
            if domain not in domain_list:
                domain_list.append(domain)

            infrastructure_info_ip = ( jmespath.search("infrastructure_info.resolving_ip[*].ip.value",
             data = data ) or [] )
            for info_ip in infrastructure_info_ip:
                if info_ip not in ip_list:
                    ip_list.append(info_ip)

            childs_url  = jmespath.search("child_urls[].url.value" , data = data ) or []
            print(f"the child url is {childs_url}")
            for url in  childs_url:
                if url not in url_list:
                    url_list.append(url)        



        elif artifact_type == "ipv4":
            ip_value = data.get("ip" , None)    
            if ip_value and ip_value not in ip_list:
                ip_list.append(ip_value)
            data["ip_type"] = data.get("ip_type" , None)

        elif artifact_type =="object":  
            data["name"] = data["object"]  
            data["node_type"] = data.get("node_type" , None)
            data["size"] = data.get("object_info", {}).get("file_size",None)
            data["file_type"] = [data.get("object_info", {}).get("file_type",None) ]  
            
            downloaded_from_url_list = jmespath.search("object_info.downloaded_from_url[].url.value" , data = data ) or []
            contacted_urls_lists = jmespath.search("object_info.contacted_url[].url.value" , data = data ) or [] 
            downloaded_from_url_list.extend(contacted_urls_lists)

            if downloaded_from_url_list and  len(downloaded_from_url_list) > 0:
                for url in downloaded_from_url_list:
                    if url not in url_list:
                        url_list.append(url)


            downloaded_from_host_list = jmespath.search("object_info.downloaded_from_host[*]",data = data) or []       
            contacted_hosts_list = jmespath.search("object_info.contacted_hosts[*]",data = data) or []     
            downloaded_from_host_list.extend(contacted_hosts_list)

            if  downloaded_from_host_list and len(downloaded_from_host_list) > 0 : 
                for obj in downloaded_from_host_list:
                    if obj.get("category" ,None): 
                        if obj.get("category") == "ip":
                            ip_value =  obj.get("value")
                            if ip_value and ip_value not in ip_list:
                                ip_list.append(ip_value)
                        elif obj.get("category") == "domain":
                            domain_value =  obj.get("value")
                            if domain_value and domain_value not in domain_list:
                                domain_list.append(domain_value)
        print(ip_list)
        if len(domain_list) < 1:
            data["domain"] = None
        else:
            data["domain"] = domain_list
        if len(ip_list) < 1:
            data["ip"] = None
        else:
            data["ip"] = ip_list
        if len(url_list) < 1:
            data["url"] = None
        else:
            data["url"] = url_list
        if len(data["object"]) < 1:
             data["object"] = None

        return data
    except Exception as e:
       logger.error(f"Exception occurred: {str(e)}")
       logger.error(f"Traceback: {traceback.format_exc()}")



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