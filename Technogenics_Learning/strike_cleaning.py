from elasticsearch import Elasticsearch
import json
from elasticsearch_dsl.connections import connections

es = connections.create_connection(
            hosts=f'https://'
                  f'{"elastic"}:'
                  f'{"JjX7K7FdRe197c2HCP3K16p2"}@'
                  f'{'localhost:9200'}',
            verify_certs=False, timeout=10, max_retries=5,
            retry_on_timeout=True,
            ssl_show_warn=False)
try:
    if es.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Failed to connect to Elasticsearch.")
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")


strikes_info= [

      {

        "name": "STA1447 - Sofacy Delivers Zebrocy Downloader",

        "createdAt": 1615277132.475124,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA1473 - TESTING APT Attack In the Middle East: The Big Bang",

        "createdAt": 1617964362.311294,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA1473 - (Test1) APT Attack In the Middle East: The Big Bang",

        "createdAt": 1617965312.876694,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA1398 - APT Nazar Delivers Nazar Trojan",

        "createdAt": 1619171603.073211,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1496 - Evilnum Malware Attack",

        "createdAt": 1619681136.53723,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA1517 - AgentTesla Targets Spain",

        "createdAt": 1620033360.798996,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRW1530 - HYDRA Ransomware Targets US",

        "createdAt": 1621928113.487927,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1531 - SWEED Delivers AgentTesla In Turkey",

        "createdAt": 1621938215.056388,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1082 - Mirai Active DDoS malware",

        "createdAt": 1623061083.930303,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA1377 - DoNot Team Delivers Trojan Via MalDoc",

        "createdAt": 1623061085.828847,

        "verified": False,

        "__typename": "Strike"
      },

      {

        "name": "SMW1496: A deep look at Evilnum and its toolset (Copy-1)",

        "createdAt": 1623061100.425942,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1496: A deep look at Evilnum and its toolset (Copy-2)",

        "createdAt": 1623061104.454195,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1571 - Unknown Threat Actor Targets UAE Firms By Exploiting Microsoft Exchange Server",

        "createdAt": 1628169026.268773,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRW1580 - Statically Compiled Variants of Linux Based Malware Rekoobe",

        "createdAt": 1629449936.552931,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRE1708 (HTTPS) - Attackers are exploiting zero day RCE flaw to target Windows users",

        "createdAt": 1631284527.585937,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRW1692(HTTPS) - LockBit Ransomware Targets Accenture",

        "createdAt": 1631691600.797652,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRW1675(HTTPS) - AvosLocker enters the ransomware scene asks for partners",

        "createdAt": 1631691891.447731,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRW1707 (HTTPS) - REvil Ransomware Latest Variant ITW",

        "createdAt": 1631692099.9362,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRW1697(HTTPS) - Chaos Ransomware Builder v4 rebranding it as Astra Ransomware",

        "createdAt": 1631692273.425945,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1732 - Pakistani Financial Institute Targeted by Unknown Threat Actor old",

        "createdAt": 1635684302.280076,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA1231 - APT34 Delivers TONEDEAF 2.0 To US Companies",

        "createdAt": 1609757971.432643,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1232 - CrowdStrike Report 2019 Marked as Malicious",

        "createdAt": 1613403781.738367,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW1445 - RCtrl Backdoor Delivered By APT30",

        "createdAt": 1614596877.603358,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRV1874 - Unknown Threat Actor Targets Australia With AsyncRAT Followed By Follina Exploitation Testing",

        "createdAt": 1654342824.654115,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA3087 - Unveiling Sea Turtle: Sophisticated Cyber Threats and DNS Hijacking",

        "createdAt": 1703844989.310919,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW4137 - BlankGrabber Malware Stealing Login Credentials And Sensitive Data",

        "createdAt": 1708067648.136829,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA4139 - Water Curupira Distributing PikaBot Malware Via Phishing",

        "createdAt": 1708069167.275584,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW4149 - NoaBot Botnet Targeting SSH Servers For Crypto Mining",

        "createdAt": 1708674259.915732,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW4189 - AceCryptor Packed Rescoms Malware Targets Europe",

        "createdAt": 1711448325.520598,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW4249 - Fickle Stealer Distributed Via Multiple Attack Chain",

        "createdAt": 1720161920.16216,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA4250 - Naikon Targets Telecoms Operators With Rainyday Malware",

        "createdAt": 1720162190.542076,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SMW4270 - Connecio Stealer Delivered Through Fake Falcon Sensor Update Lure",

        "createdAt": 1724395405.558209,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA4272 - MuddyWater Target Middle East With BugSleep",

        "createdAt": 1724396269.529956,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "STA4278 - APT41 Targets Taiwanese Government Research Institute with ShadowPad",

        "createdAt": 1725278772.94356,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRTS - Benign Strike 01",

        "createdAt": 1732860480.224667,

        "verified": False,

        "__typename": "Strike"

      },

      {

        "name": "SRTS - Benign Strike 02",

        "createdAt": 1732860516.613323,

        "verified": False,

        "__typename": "Strike"

      }

    ]
 
strikes = [] 
strikes_id = []
for str in strikes_info:
    strikes.append(str["name"])
    strike_id = str["name"].split(' - ')[0]
    strikes_id.append(strike_id)
    # print(str['name'])
print(strikes_id)
print(strikes)
    
# print(json.dumps(strikes, indent=2))

# print(json.dumps(strikes_id, indent=2))

index = "intelligence_kb_artifact*"
query = {
 "query": {
   "bool": {
     "should": [
      {
        "terms": {
          "strike.keyword" :[
              "STA1447 - Sofacy Delivers Zebrocy Downloader", "STA1473 - TESTING APT Attack In the Middle East: The Big Bang", "STA1473 - (Test1) APT Attack In the Middle East: The Big Bang", "STA1398 - APT Nazar Delivers Nazar Trojan", "SMW1496 - Evilnum Malware Attack", "STA1517 - AgentTesla Targets Spain", "SRW1530 - HYDRA Ransomware Targets US", "SMW1531 - SWEED Delivers AgentTesla In Turkey", "SMW1082 - Mirai Active DDoS malware", "STA1377 - DoNot Team Delivers Trojan Via MalDoc", "SMW1496: A deep look at Evilnum and its toolset (Copy-1)", "SMW1496: A deep look at Evilnum and its toolset (Copy-2)", "SMW1571 - Unknown Threat Actor Targets UAE Firms By Exploiting Microsoft Exchange Server", "SRW1580 - Statically Compiled Variants of Linux Based Malware Rekoobe", "SRE1708 (HTTPS) - Attackers are exploiting zero day RCE flaw to target Windows users", "SRW1692(HTTPS) - LockBit Ransomware Targets Accenture", "SRW1675(HTTPS) - AvosLocker enters the ransomware scene asks for partners", "SRW1707 (HTTPS) - REvil Ransomware Latest Variant ITW", "SRW1697(HTTPS) - Chaos Ransomware Builder v4 rebranding it as Astra Ransomware", "SMW1732 - Pakistani Financial Institute Targeted by Unknown Threat Actor old", "STA1231 - APT34 Delivers TONEDEAF 2.0 To US Companies", "SMW1232 - CrowdStrike Report 2019 Marked as Malicious", "SMW1445 - RCtrl Backdoor Delivered By APT30", "SRV1874 - Unknown Threat Actor Targets Australia With AsyncRAT Followed By Follina Exploitation Testing", "STA3087 - Unveiling Sea Turtle: Sophisticated Cyber Threats and DNS Hijacking", "SMW4137 - BlankGrabber Malware Stealing Login Credentials And Sensitive Data", "STA4139 - Water Curupira Distributing PikaBot Malware Via Phishing", "SMW4149 - NoaBot Botnet Targeting SSH Servers For Crypto Mining", "SMW4189 - AceCryptor Packed Rescoms Malware Targets Europe", "SMW4249 - Fickle Stealer Distributed Via Multiple Attack Chain", "STA4250 - Naikon Targets Telecoms Operators With Rainyday Malware", "SMW4270 - Connecio Stealer Delivered Through Fake Falcon Sensor Update Lure", "STA4272 - MuddyWater Target Middle East With BugSleep", "STA4278 - APT41 Targets Taiwanese Government Research Institute with ShadowPad", "SRTS - Benign Strike 01", "SRTS - Benign Strike 02"]
      }
      },
      {      
        "terms": {
          "strike_id.keyword": [
            "STA1447",
            "STA1473",
            "STA1473",
            "STA1398",
            "SMW1496",
            "STA1517",
            "SRW1530",
            "SMW1531",
            "SMW1082",
            "STA1377",
            "SMW1496: A deep look at Evilnum and its toolset (Copy-1)",
            "SMW1496: A deep look at Evilnum and its toolset (Copy-2)",
            "SMW1571",
            "SRW1580",
            "SRE1708 (HTTPS)",
            "SRW1692(HTTPS)",
            "SRW1675(HTTPS)",
            "SRW1707 (HTTPS)",
            "SRW1697(HTTPS)",
            "SMW1732",
            "STA1231",
            "SMW1232",
            "SMW1445",
            "SRV1874",
            "STA3087",
            "SMW4137",
            "STA4139",
            "SMW4149",
            "SMW4189",
            "SMW4249",
            "STA4250",
            "SMW4270",
            "STA4272",
            "STA4278",
            "SRTS",
            "SRTS"
            ]
        }
      } 
      ]
    }
  }
}

resp = es.search(index=index, body=query, size=2000)
hits = resp['hits']['hits']
print(len(hits))

for hit in hits:
    doc_id = hit['_id']
    index_name = hit['_index']
    name = hit['_source']['name']
    strike_ids = hit['_source'].get('strike_id',[])
    new_strike_ids = []
    strikes = hit['_source'].get('strike', [])
    new_strikes = []
    for strike_id in strike_ids:
        if strike_id not  in strikes_id:
            new_strike_ids.append(strike_id)
    
    for strike in strikes:
        if strike not in strikes:
            new_strikes.append(strike)

    # Define the update script or partial document
    update_body = {
        "doc": {
            "strike_id": new_strike_ids,
            "strike": new_strikes,
            "strike_count": len(new_strike_ids)
        }
    }
    print(name)
    print(update_body)



    es.update(index=index_name, id=doc_id, body=update_body)


# print(json.dumps(hits, indent=2))

