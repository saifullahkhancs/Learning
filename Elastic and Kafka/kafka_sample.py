from confluent_kafka import Producer, Consumer, KafkaException
from elasticsearch import Elasticsearch,helpers
from elasticsearch.exceptions import TransportError, ConnectionError, NotFoundError
import json
import random
from datetime import datetime
# Producer configuration
producer_conf = {
    'bootstrap.servers': 'localhost:29092'
}

try:
    producer = Producer(producer_conf)
except Exception as e:
    print(f"Error connecting to kafka: {e}")

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced:", msg.value().decode())
        print(f"Message delivered to {msg.topic()}  [{msg.partition()}]")

# Send a message
# producer.produce('test-topic', key='key', value='Hello, Kafka!',  callback = acked)
# producer.poll(1)
data2 = {  "name":"cadosecurity",  "url": "https://www.cadosecurity.com/blog/investigating-docker-hijacking-malware-a-deep-dive-into-elf-binary-analysis-part2",  "title": "Part 2: Investigating Docker Hijacking Malware - A Deep Dive into ELF Binary Analysis",  "type":"news",  "subscriptions":[    "67111ec7bf32fcbb8dc90408"  ],  "rules":[    {      "type":"snort",      "rule":{        "identifier":"2034648",        "rule":"alert tcp any any -> [$HOME_NET,$HTTP_SERVERS] any (msg:”ET EXPLOIT Apache log4j RCE Attempt (http rmi) (CVE-2021-44228)”; flow:established,to_server; content:”|24 7b|jndi|3a|rmi|3a 2f 2f|”; nocase; fast_pattern; reference:url,lunasec.io/docs/blog/log4j-zero-day/; reference:cve,2021-44228; classtype:attempted-admin; sid:2034648; rev:1; metadata:attack_target Server, created_at 2021_12_10, cve CVE_2021_44228, deployment Perimeter, deployment Internal, former_category EXPLOIT, signature_severity Major, tag Exploit, updated_at 2021_12_10;)"      }    }  ],  "artifacts":[    {      "type":"url",      "artifact":"lunasec.io/docs/blog/log4j-zero-day/"    },    {      "type":"url",      "artifact":"https://oppo.com"    }  ]} 
data1 = {
   "name":"cadosecurity",
   "type":"news",
   "subscriptions":[
      "670e7f5fb00ebe2534cb8798"
   ],
   "iocs":{
      "rules":[
         {
            "type":"snort",
            "rule":{
               "identifier":"2034648",
               "rule":"alert tcp any any -> [$HOME_NET,$HTTP_SERVERS] any (msg:”ET EXPLOIT Apache log4j RCE Attempt (http rmi) (CVE-2021-44228)”; flow:established,to_server; content:”|24 7b|jndi|3a|rmi|3a 2f 2f|”; nocase; fast_pattern; reference:url,lunasec.io/docs/blog/log4j-zero-day/; reference:cve,2021-44228; classtype:attempted-admin; sid:2034648; rev:1; metadata:attack_target Server, created_at 2021_12_10, cve CVE_2021_44228, deployment Perimeter, deployment Internal, former_category EXPLOIT, signature_severity Major, tag Exploit, updated_at 2021_12_10;)"
            }
         }
      ],
      "artifacts":[
         {
            "type":"url",
            "artifact":"lunasec.io/docs/blog/log4j-zero-day/"
         },
         {
            "type":"url",
            "artifact":"https://oppo.com"
         }
      ]
   }
}
event_data ={
    "title": "blog title",
    "threat_url": "blog url",
    "source_type": "news",
    "source_name": "cadosecurity",
    "artifacts": [
        {
            "type": "domain",
            "artifact": "qaengineer.com"
        },
        {
            "type": "domain",
            "artifact": "www.samsung.com"
        }
    ],
    "rules": [
        {
            "type": "snort",
            "rule": {
                "identifier": "2034648",
                "rule": "alert tcp any any -> [$HOME_NET,$HTTP_SERVERS] any (msg:”ET EXPLOIT Apache log4j RCE Attempt (http rmi) (CVE-2021-44228)”; flow:established,to_server; content:”|24 7b|jndi|3a|rmi|3a 2f 2f|”; nocase; fast_pattern; reference:url,lunasec.io/docs/blog/log4j-zero-day/; reference:cve,2021-44228; classtype:attempted-admin; sid:2034648; rev:1; metadata:attack_target Server, created_at 2021_12_10, cve CVE_2021_44228, deployment Perimeter, deployment Internal, former_category EXPLOIT, signature_severity Major, tag Exploit, updated_at 2021_12_10;)"
            }
        },
        {
            "type": "snort",
            "rule": {
                "identifier": "2034647",
                "rule": "alert tcp any any -> [$HOME_NET,$HTTP_SERVERS] any (msg:”ET EXPLOIT Apache log4j RCE Attempt (http ldap) (CVE-2021-44228)”; flow:established,to_server; content:”|24 7b|jndi|3a|ldap|3a 2f 2f|”; nocase; fast_pattern; reference:url,lunasec.io/docs/blog/log4j-zero-day/; reference:cve,2021-44228; classtype:attempted-admin; sid:2034647; rev:1; metadata:attack_target Server, created_at 2021_12_10, cve CVE_2021_44228, deployment Perimeter, deployment Internal, former_category EXPLOIT, signature_severity Major, tag Exploit, updated_at 2021_12_10;)"
            }
        }
    ],
    "cves": [
        {
            "type": "cve",
            "artifact": "CVE-2026-56558"
        },
        {
            "type": "cve",
            "artifact": "CVE-2021-44228"
        }
    ]
}

test_data  = {"data": {"title": "Using gRPC and HTTP/2 for Cryptominer Deployment: An Unconventional Approach", "threat_url": "https://www.trendmicro.com/en_us/research/24/j/using-grpc-http-2-for-cryptominer-deployment.html", "source_name": "trendmicro", "source_type": "ThreatBlogs", "artifacts": [{"type": "ipv4", "artifact": "59.93.45.16"}, {"type": "ipv4", "artifact": "167.71.194.227"}, {"type": "object", "artifact": "0d4eb69b551cb538a9a4c46f7b57906a47bcabb8ef8a5d245584fbba09fc5084"}], "rules": [], "cves": []}}
data = json.dumps(test_data).encode('utf-8')




topic  = "logs"
log_levels = ['DEBUG', 'INFO', 'WARN', 'ERROR']
sources = ['application', 'system']
messages = [
    'User login successful', 'User login failed', 'Database connection established',
    'Error reading from file', 'Service started', 'Service stopped',
    'Unexpected error occurred', 'Configuration updated', 'Resource not found',
    'File uploaded', 'Timeout while connecting', 'Permission denied',
    'Server overload', 'Session expired', 'Cache cleared', 'Data synchronized'
]

# Function to generate log messages
def generate_log():
    return {
        "timestamp":  int(datetime.now().timestamp ()*1000) ,
        "log_level": random.choice(log_levels),
        "message": random.choice(messages),
        "source": random.choice(sources)
    }

# Generate a list of 15-20 log messages
log_messages = [generate_log() for _ in range(random.randint(15, 20))]
message = log_messages[0]
# Convert log messages to JSON format
data = json.dumps(message)

print(data)

producer.produce(topic , key = "key",  value= data , callback = acked )
producer.poll(1)





# Subscribe to the topic
# consumer.subscribe(['test-topic'])

# # Read messages
# try:
#     while True:
#         message = consumer.poll(1.0)  # Poll for 1 second
#         if message is None:
#             continue
#         if message.error():
#             raise KafkaException(message.error())
#         else:
            


#             print(f"Received message: {message.value().decode()}")
# finally:
#     # Close the consumer on exit
#     consumer.close()
