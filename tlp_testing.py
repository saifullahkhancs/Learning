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




tlp_object_testing_object = {
    "meta": {
        "timestamp": 1732789800351,
        "username": "neo4j",
        "txId": 400000001,
        "txEventId": 0,
        "txEventsCount": 1,
        "operation": "created",
        "source": {
            "hostname": "neo4j-cluster-core-0"
        }
    },
    "payload": {
        "id": "25704370",
        "before": None,
        "after": {
            "properties": {
                "confidence": "high",
                "createdAt": 1732789798.937477,
                "firstSeen": 1732783800.6,
                "is_deployable": True,
                "lastSeen": 1732783800.6,
                "md5": "a91b4875630c4f702ab63f94ed633da4",
                "name": "object-08e3bb63-f53d-4446-81b0-862be6b6bcda",
                "score": 90,
                "sha256": "d864a359e3a19182e72109fe75408d21b10215938e8be4098c4dbbc8ce0b7c7c",
                "srid": "object-08e3bb63-f53d-4446-81b0-862be6b6bcda",
                "uid": "08e3bb63-f53d-4446-81b0-862be6b6bcda",
                "updatedAt": 1732789800.351733,
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
            "is_deployable": "Boolean",
            "lastSeen": "Double",
            "md5": "String",
            "name": "String",
            "score": "Integer",
            "sha256": "String",
            "srid": "String",
            "uid": "String",
            "updatedAt": "Double",
            "verdict": "String"
        },
        "constraints": [
            {
                "label": "Object",
                "properties": ["srid"],
                "type": "UNIQUE"
            },
            {
                "label": "Object",
                "properties": ["uid"],
                "type": "UNIQUE"
            },
            {
                "label": "Object",
                "properties": ["name"],
                "type": "UNIQUE"
            }
        ]
    }
}

tlp_object_testing_tlp = {
    "meta": {
        "timestamp": 1681809387168,
        "username": "neo4j",
        "txId": 400000002,
        "txEventId": 0,
        "txEventsCount": 1,
        "operation": "created",
        "source": {
            "hostname": "neo4j-cluster-core-0"
        }
    },
    "payload": {
        "id": "5948438",
        "before": None,
        "after": {
            "properties": {
                "createdAt": 1681809387.168197,
                "name": "white",
                "srid": "60d08279-24f1-472b-a8e8-eb0c26f5e3de",
                "uid": "9440be15-a596-4151-bfe4-fcf155572ed8",
                "updatedAt": 1681809387.168209
            },
            "labels": ["TLP"]
        },
        "type": "node"
    },
    "schema": {
        "properties": {
            "createdAt": "Double",
            "name": "String",
            "srid": "String",
            "uid": "String",
            "updatedAt": "Double"
        },
        "constraints": [
            {
                "label": "TLP",
                "properties": ["srid"],
                "type": "UNIQUE"
            },
            {
                "label": "TLP",
                "properties": ["uid"],
                "type": "UNIQUE"
            }
        ]
    }
}


tlp_object_testing_object_with_tlp = {
    "meta": {
        "timestamp": 1732789800352,
        "username": "neo4j",
        "txId": 400000003,
        "txEventId": 0,
        "txEventsCount": 1,
        "operation": "created",
        "source": {
            "hostname": "neo4j-cluster-core-0"
        }
    },
    "payload": {
        "id": "371934102",
        "start": {
            "id": "25704370",
            "labels": ["Object"],
            "ids": {
                "srid": "object-08e3bb63-f53d-4446-81b0-862be6b6bcda"
            }
        },
        "end": {
            "id": "5948438",
            "labels": ["TLP"],
            "ids": {
                "srid": "60d08279-24f1-472b-a8e8-eb0c26f5e3de"
            }
        },
        "before": None,
        "after": {
            "properties": {
                "createdAt": 1732789800.351733,
                "updatedAt": 1732789800.351733
            }
        },
        "label": "HAS_TLP",
        "type": "relationship"
    },
    "schema": {
        "properties": {
            "createdAt": "Double",
            "updatedAt": "Double"
        }
    }
}


enrich_event = {
    "workspace_id": "d045390b-f028-4dd2-8a67-5786bd1ba792",
    "company_id": "23ea8442-ae2a-4cca-a115-1220f6116eb6",
    "user_id": "ace9c2c2-2ea6-4f78-9e76-0bee4716263a",
    "label": "Enrich artifacts",
    "description": "Enriched artifacts from AE",
    "success": True,
    "timestamp": 1731481869.185883,
    "type": "info",
    "metadata": {
        "plan_id": None,
        "job_id": None,
        "task_id": None,
        "action": {
            "name": "enrichment",
            "integration": None,
            "source": None
        },
        "resource": {
            "id": "6705154e375775a70ce7ff79",
            "entity": "Intel",
            "type": "sha256",
            "value": "42efd4351f45ff1b2fb5848282c14e94657e8e9c26862d35a19dd6787377f1f7",
            "rule": None,
            "tags": [],
            "custom_score": None,
            "analysis_state": "completed",
            "analysis": {
                "community_verdict": "clean",
                "community_score": 1,
                "free_verdict": "no verdict",
                "free_score": 0,
                "premium_verdict": "no verdict",
                "premium_score": 0,
                "strike_ready_verdict": "clean",
                "strike_ready_score": 1,
                "strike_ready_tlp": "WHITE"
            },
            "object": {
                "md5": "72219ba421752aa1e96e0b01fb217f51",
                "sha1": "550c893e54273f1303bf7ac6255c6727839622b5",
                "sha256": "42efd4351f45ff1b2fb5848282c14e94657e8e9c26862d35a19dd6787377f1f7"
            },
            "hash": None
        }
    }
}



# topic  = "elastic"
topic= "registered_user_thre"
if __name__ == "__main__":

    # for k in range(150):
    #     for i in range(3):
    registered_user = object
    response = producer.send(topic,tlp_object_testing_object_with_tlp )
    print(response.get())
    time.sleep(5)
