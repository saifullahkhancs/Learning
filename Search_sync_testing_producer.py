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
    "operation": "create",
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
        "md5": "",
        "name": "object-2017dec5-650c-4944-8322-81164f0bc3ec",
        "score": 10,
        "sha1": "",
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
    "constraints": [
      {
        "label": "Object",
        "properties": ["uid"],
        "type": "UNIQUE"
      },
      {
        "label": "Object",
        "properties": ["srid"],
        "type": "UNIQUE"
      },
      {
        "label": "Object",
        "properties": ["name"],
        "type": "UNIQUE"
      },
      {
        "label": "Object",
        "properties": ["srid"],
        "type": "NODE_PROPERTY_EXISTS"
      },
      {
        "label": "SHA1",
        "properties": ["name"],
        "type": "UNIQUE"
      },
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
        "properties": ["srid"],
        "type": "NODE_PROPERTY_EXISTS"
      }
    ]
  }
}



sha_ransom = {
  "meta": {
    "timestamp": 1704646392548,
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
    "id": "6313",
    "before": None,
    "after": {
      "properties": {
        "firstSeen": 1704646392.448,
        "lastSeen": 1704646392.548,
        "name": "c2cc9ad6549d7e81f9052ba45680219bab75960a",
        "sourceId": 6313,
        "srid": "sha1-00fd6e30-e09d-43b0-817c-589633522546",
        "uid": "f0ed9f49-2f39-4088-b3e0-a94be91e73e6"
      },
      "labels": ["SHA1"]
    },
    "type": "node"
  },
  "schema": {
    "properties": {
      "firstSeen": "Double",
      "lastSeen": "Double",
      "name": "String",
      "sourceId": "Long",
      "srid": "String",
      "uid": "String"
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


raansom = {
  "meta": {
    "timestamp": 1704646393000,
    "username": "neo4j",
    "txId": 12348,
    "txEventId": 0,
    "txEventsCount": 1,
    "operation": "created",
    "source": {
      "hostname": "neo4j-cluster-core-0"
    }
  },
  "payload": {
    "id": "721",
    "before": None,
    "after": {
      "properties": {
        "alias": ["malware-gen", "armageddon"],
        "authentiHash": "0a73616ec491081fdc9c2b6fd696ca8cee7101c715636f99a91ec27ce578de32",
        "creator": "darkday",
        "date": "June 13th, 2019",
        "description": "Armageddon is a ransomware infection, that does not add an extension or rename files in any other way. Armageddon is distributed using third-party software download sources, spam email campaigns, trojans, fake software updaters, and cracks. Once infiltrated, Armageddon encrypts most of the stored files using the RSA-2048 encryption algorithm. Once data is encrypted, Armageddon opens a pop-up window that contains a ransom-demand message.",
        "encryption": "No Information",
        "extensions": [],
        "family": "HiddenTear",
        "fileSize": "322 KB (329,728 Bytes)",
        "fileType": "Win32 PE executable (.EXE)",
        "impHash": "f34d5f2d4577ed6d9ceec516c1f5a744",
        "md5": "50c6225ff8e1e741238fc0bbdf7d8172",
        "name": "Armageddon",
        "origin": "No Information",
        "paymentMethod": "No Information",
        "platform": ["windows"],
        "price": "No Information",
        "ransomNote": [],
        "ransomwareExtension": "",
        "refs": ["https://malware.wikia.org/wiki/Armageddon"],
        "sha1": "c2cc9ad6549d7e81f9052ba45680219bab75960a",
        "sha256": "1ebdbfea6ab13f258a7d00dea47de48261cfb84d52ebbb6f282498c3ab1b1b39",
        "sourceId": 721,
        "sourceLanguage": "Assembly",
        "srid": "ransom-armageddon-e5d1ce62-82e9-4724-a75c-8e0802ba9f2f",
        "ssDeep": "3072:F66/pFINPVP06dvuqrWrb60Db+7uQxQrq61gFsRd8cQUewkoLeC8BS0HVKT+8X2C:Gbxu6Q31gFsR0FoTY8T+8Gx",
        "uid": "bca91af5-687e-47fc-9917-86357e96e07c",
        "vHash": "235036751512b099322b6043"
      },
      "labels": ["Ransom"]
    },
    "type": "node"
  },
  "schema": {
    "properties": {
      "alias": "List<String>",
      "authentiHash": "String",
      "creator": "String",
      "date": "String",
      "description": "String",
      "encryption": "String",
      "extensions": "List<String>",
      "family": "String",
      "fileSize": "String",
      "fileType": "String",
      "impHash": "String",
      "md5": "String",
      "name": "String",
      "origin": "String",
      "paymentMethod": "String",
      "platform": "List<String>",
      "price": "String",
      "ransomNote": "List<String>",
      "ransomwareExtension": "String",
      "refs": "List<String>",
      "sha1": "String",
      "sha256": "String",
      "sourceId": "Long",
      "sourceLanguage": "String",
      "srid": "String",
      "ssDeep": "String",
      "uid": "String",
      "vHash": "String"
    },
    "constraints": [
      {
        "label": "Ransom",
        "properties": ["uid"],
        "type": "UNIQUE"
      },
      {
        "label": "Ransom",
        "properties": ["srid"],
        "type": "UNIQUE"
      },
      {
        "label": "Ransom",
        "properties": ["sha1"],
        "type": "UNIQUE"
      },
      {
        "label": "Ransom",
        "properties": ["name"],
        "type": "UNIQUE"
      }
    ]
  }
}



rasnsom_sha_rel = {
  "meta": {
    "timestamp": 1704646393000,
    "username": "neo4j",
    "txId": 12349,
    "txEventId": 0,
    "txEventsCount": 1,
    "operation": "created",
    "source": {
      "hostname": "neo4j-cluster-core-0"
    }
  },
  "payload": {
    "id": "44148",
    "end": {
      "id": "6313",
      "labels": ["SHA1"],
      "ids": {
        "name": "c2cc9ad6549d7e81f9052ba45680219bab75960a"
      }
    },
    "start": {
      "id": "721",
      "labels": ["Ransom"],
      "ids": {
        "name": "Armageddon"
      }
    },
    "before": None,
    "after": {
      "properties": {
        "sourceId": 44148,
        "createdAt": 1704646393.000,
        "updatedAt": 1704646393.000
      }
    },
    "label": "RANSOM_SHA1",
    "type": "relationship"
  },
  "schema": {
    "properties": {
      "sourceId": "Long",
      "createdAt": "Double",
      "updatedAt": "Double"
    },
    "constraints": []
  }
}


sha_ransom_rel  = {
  "meta": {
    "timestamp": 1704646394000,
    "username": "neo4j",
    "txId": 12350,
    "txEventId": 0,
    "txEventsCount": 1,
    "operation": "created",
    "source": {
      "hostname": "neo4j-cluster-core-0"
    }
  },
  "payload": {
    "id": "44149",
    "start": {
      "id": "6313",
      "labels": ["SHA1"],
      "ids": {
        "name": "c2cc9ad6549d7e81f9052ba45680219bab75960a"
      }
    },
    "end": {
      "id": "721",
      "labels": ["Ransom"],
      "ids": {
        "name": "Armageddon"
      }
    },
    "before": None,
    "after": {
      "properties": {
        "sourceId": 44149,
        "createdAt": 1704646394.000,
        "updatedAt": 1704646394.000
      }
    },
    "label": "SHA1_OF_RANSOM",
    "type": "relationship"
  },
  "schema": {
    "properties": {
      "sourceId": "Long",
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
    response = producer.send(topic, object_has_sha) 
    print(response.get())
    time.sleep(5)
