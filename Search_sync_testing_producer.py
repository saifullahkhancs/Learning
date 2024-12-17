import json
from kafka import KafkaProducer
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

import logging

# Configure logging for Kafka library
logger = logging.getLogger('kafka')
logger.setLevel(logging.INFO)  # Set the desired log level

# Create a console handler and set its level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set the desired log level

# Create a formatter and add it to the console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the Kafka logger
logger.addHandler(console_handler)



producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    # api_version=(0, 11, 5),
    value_serializer=json_serializer,
    # sasl_plain_username='tg-user1',
    # sasl_plain_password='tg-pass1', sasl_mechanism='PLAIN',
    # security_protocol='SASL_PLAINTEXT'
)



object = {"meta": {
    "timestamp": 1676544118775,
    "username": "neo4j",
    "txId": 12345,
    "txEventId": 0,
    "txEventsCount": 1,
    "operation": "created",
    "source": {
      "hostname": "neo4j-cluster-core-0"
    }
  },
  "payload": {
    "id": "240151",
    "before": None,
    "after": {
      "properties": {
        "confidence": "high",
        "createdAt": 1676544118.77552,
        "firstSeen": 1676543582.9,
        "lastSeen": 1676543582.9,
        "md5": "e56093a7cd414f5592cc76a41ddd4c25",
        "name": "object-2017dec5-650c-4944-8322-81164f0bc3ec",
        "score": 90,
        "sha1": "c1788dfd2f4faea8dc64652149b7190b714a9450",
        "sha256": "107b4465806250a6fd7fda62b3ec399b4eaa97a7262bd4a9e13fbe96007ed99e",
        "srid": "object-2017dec5-650c-4944-8322-81164f0bc3ec",
        "uid": "2017dec5-650c-4944-8322-81164f0bc3ec",
        "updatedAt": 1696633853.034841,
        "verdict": "malicious"
      },
      "labels": ["Object"]
    },
    "type": "node"
  },
  "schema": {
    "properties": {
      "confidence": "String",
      "createdAt": "Double",
      "firstSeen": "Double",
      "lastSeen": "Double",
      "md5": "String",
      "name": "String",
      "score": "Integer",
      "sha1": "String",
      "sha256": "String",
      "srid": "String",
      "uid": "String",
      "updatedAt": "Double",
      "verdict": "String"
    },
  }
}

sha1 = {
  "meta": {
    "timestamp": 1676544119045,
    "username": "neo4j",
    "txId": 12346,
    "txEventId": 0,
    "txEventsCount": 1,
    "operation": "created",
    "source": {
      "hostname": "neo4j-cluster-core-0"
    }
  },
  "payload": {
    "id": "468180",
    "before": None,
    "after": {
      "properties": {
        "createdAt": 1676544119.045492,
        "firstSeen": 1676543582.9,
        "lastSeen": 1676543582.9,
        "name": "c1788dfd2f4faea8dc64652149b7190b714a9450",
        "srid": "sha1-0bb6d767-80a2-4c63-bd22-cf195cb29f7e",
        "uid": "0bb6d767-80a2-4c63-bd22-cf195cb29f7e",
        "updatedAt": 1676544119.045492
      },
      "labels": ["SHA1"]
    },
    "type": "node"
  },
  "schema": {
    "properties": {
      "createdAt": "Double",
      "firstSeen": "Double",
      "lastSeen": "Double",
      "name": "String",
      "srid": "String",
      "uid": "String",
      "updatedAt": "Double"
    },
    "constraints": [
      {
        "label": "SHA1",
        "properties": ["uid"],
        "type": "UNIQUE"
      },
      {
        "label": "SHA1",
        "properties": ["srid"],
        "type": "UNIQUE"
      },
      {
        "label": "SHA1",
        "properties": ["name"],
        "type": "UNIQUE"
      }
    ]
  }
}


md5 = {
    "meta": {
        "timestamp": 17303823028809,
        "username": "neo4j",
        "txId": 396892500,
        "txEventId": 0,
        "txEventsCount": 1,
        "operation": "created",
        "source": {
            "hostname": "neo4j-cluster-core-0"
        }
    },
    "payload": {
        "id": "260959378",
        "before":None,
        "after": {
            "properties": {
                "uid": "74d568fd-c219-4ecd-9afb-75e917452279",
                "createdAt": 1.730382302690152E9,
                "name": "e56093a7cd414f5592cc76a41ddd4c25",
                "srid": "md5-74d568fd-c219-4ecd-9afb-75e917452279",
                "updatedAt": 1.730382302690152E9,
                "strike" :["STA123","STA5029"]
            },
            "labels": [
                "MD5"
            ]
        },
        "type": "node"
    },
    "schema": {
        "properties": {
            "uid": "String",
            "createdAt": "Double",
            "name": "String",
            "srid": "String",
            "updatedAt": "Double",
            "strike": "List"
        },
        "constraints": [
            {
                "label": "MD5",
                "properties": [
                    "uid"
                ],
                "type": "UNIQUE"
            },
            {
                "label": "MD5",
                "properties": [
                    "srid"
                ],
                "type": "UNIQUE"
            },
            {
                "label": "MD5",
                "properties": [
                    "name"
                ],
                "type": "UNIQUE"
            },
            {
                "label": "MD5",
                "properties": [
                    "srid"
                ],
                "type": "NODE_PROPERTY_EXISTS"
            }
        ]
    }
} 




object_has_sha = {
  "meta": {
    "timestamp": 1676544119083,
    "username": "neo4j",
    "txId": 12347,
    "txEventId": 0,
    "txEventsCount": 1,
    "operation": "created",
    "source": {
      "hostname": "neo4j-cluster-core-0"
    }
  },
  "payload": {
    "id": "1293324",
    "start": {
      "id": "240151",
      "labels": ["Object"],
      "ids": {
        "srid": "object-2017dec5-650c-4944-8322-81164f0bc3ec"
      }
    },
    "end": {
      "id": "468180",
      "labels": ["SHA1"],
      "ids": {
        "name": "c1788dfd2f4faea8dc64652149b7190b714a9450"
      }
    },
    "before": None,
    "after": {
      "properties": {
        "createdAt": 1676544119.083627,
        "updatedAt": 1676544119.083627
      }
    },
    "label": "HAS_SHA1",
    "type": "relationship"
  },
  "schema": {
    "properties": {
      "createdAt": "Double",
      "updatedAt": "Double"
    },
    "constraints": []
  }
}






# topic  = "elastic"
topic= "registered_user_thre"
if __name__ == "__main__":

    # for k in range(150):
    #     for i in range(3):
    registered_user = object
    response = producer.send(topic,sha1 )
    print(response.get())
    time.sleep(5)
