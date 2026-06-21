from shared.kafka_utils import create_producer, send_event

producer = create_producer(bootstrap_servers='localhost:29092')




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
                "strike_ready_tlp": "white",
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

new_enrich = {
  "workspace_id": "8c477159-8e8a-467d-83ac-8ac31f2218b2",
  "company_id": "23ea8442-ae2a-4cca-a115-1220f6116eb6",
  "user_id": "ace9c2c2-2ea6-4f78-9e76-0bee4716263a",
  "label": "Add Artifacts",
  "description": "Added artifacts from case",
  "success": True,
  "timestamp": 1735555669.172204,
  "type": "info",
  "metadata": {
    "plan_id": None,
    "job_id": None,
    "task_id": None,
    "action": {
      "name": "add_artifacts",
      "integration": None,
      "source": {
        "id": "SRC-14143",
        "value": "SRC-14143",
        "type": "case"
      }
    },
    "resource": {
      "id": "67727a54fc62837dd1f907df",
      "entity": "Intel",
      "type": "url",
      "value": "www.orden-justice.su/WinDiver.exe",
      "rule": None,
      "tags": [
        "Not Prevented"
      ],
      "custom_score": None,
      "analysis_state": None,
      "analysis": {},
      "object": None,
      "hash": None
    }
  }
}


new_sync_pipeline_data ={
    "meta": {
        "ver": 1.0,
        "_id": "381df1c8de9d97928c7d369525143f56161c68e6",
        "index": "ver_1.0.1_strikeready_intel_14_url"
    },
    "data": {
        "value": "https://47.90.171.145/",
        "type": "url",
        "confidence": "high",
        "sources": [
            {
                "id": "12",
                "name": "phishtank",
                "display_name": "PhishTank",
                "url": "http://www.phishtank.com/phish_detail.php?phish_id=8997660",
                "confidence": "high",
                "type": "ThreatFeed",
                "time": 1742871812.119023
            },
            {
                "id": "41",
                "name": "phishstats",
                "display_name": "PhishStats",
                "url": "https://phishstats.info:2096/api/phishing/?_p=11&_size=50&_sort=-date&_where=(date,gt,2025-03-03T00:07:29)~and(date,lt,2025-03-03T12:07:29)",
                "confidence": "medium",
                "type": "ThreatFeed",
                "time": 1741004066.367672
            },
            {
                "id": "12",
                "name": "phishtank",
                "display_name": "PhishTank",
                "url": "http://www.phishtank.com/phish_detail.php?phish_id=8997660",
                "confidence": "high",
                "type": "ThreatFeed",
                "time": 1740971020.63628
            }
        ],
        "score": 80,
        "verdict": "malicious",
        "approved": False,
        "malwares": [],
        "vulnerability": [],
        "threat_actors": [],
        "threat": [],
        "tools": [],
        "ransoms": [],
        "strikes": [],
        "tags": [],
        "internal_tags": [
            "phishing"
        ],
        "first_seen": 1740967260.2,
        "last_seen": 1741003253.431954,
        "raw": [],
        "analysis": {
            "status": [
                {
                    "value": "online",
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": 1742871812.119722,
                        "confidence": "high",
                        "type": "ThreatFeed",
                        "sr_reviewed": False
                    }
                }
            ],
            "verdict": [
                {
                    "value": "suspicious",
                    "reported_source": {
                        "name": "phishstats",
                        "reported_time": 1741004066.368228,
                        "confidence": "medium",
                        "type": "ThreatFeed",
                        "sr_reviewed": False
                    }
                },
                {
                    "value": "malicious",
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": 1742871812.119782,
                        "confidence": "high",
                        "type": "ThreatFeed",
                        "sr_reviewed": True
                    }
                }
            ],
            "confidence": [
                {
                    "value": "medium",
                    "reported_source": {
                        "name": "phishstats",
                        "reported_time": 1741004066.368252,
                        "confidence": "medium",
                        "type": "ThreatFeed",
                        "sr_reviewed": True
                    }
                },
                {
                    "value": "high",
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": 1742871812.119822,
                        "confidence": "high",
                        "type": "ThreatFeed",
                        "sr_reviewed": True
                    }
                }
            ],
            "score": [
                {
                    "value": 40,
                    "reported_source": {
                        "name": "phishstats",
                        "reported_time": 1741004066.368284,
                        "confidence": "medium",
                        "type": "ThreatFeed",
                        "sr_reviewed": False
                    }
                },
                {
                    "value": 80,
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": 1742871812.11985,
                        "confidence": "high",
                        "type": "ThreatFeed",
                        "sr_reviewed": True
                    }
                }
            ]
        },
        "presence_index": {},
        "mitigation_rules": [],
        "first_crawled": 1740971020.637223,
        "last_crawled": 1742871812.119882,
        "mitre_ttp": [],
        "tlp": "amber",
        "whitelisted_check": True,
        "internal_raw_osint": False,
        "internal_allow_sync": True,
        "associated_threat_campaigns": [],
        "is_deployable": True,
        "dark_feed": False,
        "sr_intel": False,
        "status": "online",
        "uri": "/",
        "host": {
            "value": "47.90.171.145",
            "type": "ipv4",
            "category": "ip",
            "port": None
        },
        "larted": None,
        "open_ports": [],
        "files_downloaded": [],
        "http_response": {
            "status_code": None,
            "response_len": None,
            "content_type": "",
            "filename": ""
        },
        "shortened": {
            "is_shorten": None,
            "final_location": {
                "url": {}
            },
            "redirection_chain": []
        },
        "url_content_categorization": [],
        "urls_part_of_body": [],
        "artifact_validation": [
            {
                "benign": False,
                "whitelisted": False,
                "is_deployable": True,
                "domain_rank": None,
                "date": 1742871812.300783,
                "compromised": False,
                "is_fp": False,
                "forcefully_malicious": None,
                "source": "whitelisting_service"
            },
            {
                "benign": False,
                "whitelisted": False,
                "is_deployable": True,
                "domain_rank": None,
                "date": 1741004066.468148,
                "compromised": False,
                "is_fp": False,
                "forcefully_malicious": None,
                "source": "whitelisting_service"
            },
            {
                "benign": False,
                "whitelisted": False,
                "is_deployable": True,
                "domain_rank": None,
                "date": 1740971020.730626,
                "compromised": False,
                "is_fp": False,
                "forcefully_malicious": None,
                "source": "whitelisting_service"
            }
            ]}}


after_elastic_data = {'name': 'https://47.90.171.145/', 'displayName': 'https://47.90.171.145/', 'type': 'url', 'created_at': 1745058207, 'updated_at': 1742871812, 'entity': ['url', 'artifact'], 'tag': [], 'source': ['phishtank', 'phishstats'], 'sources_count': 2, 'strike_id': [], 'first_seen': 1740967260.2, 'last_seen': 1741003253.431954, 'is_deployable': True, 'kb_verdict': 'malicious', 'kb_score': 80, 'cve': [], 'category': [], 'targeted_organization': [], 'targets_sector': [], 'targeted_industry': [], 'targets_region': [], 'targeted_country': [], 'attack_origin': [], 'source_type': ['ThreatFeed'], 'tlp': ['amber'], 'url': ['https://47.90.171.145/'], 'ip': ['47.90.171.145']}
# topic  = "elastic"
topic = "after_elastic"
# topic= "registered_user_thre"      # for adding relation
# topic = "registered_user__intel_"    #   for enrichment
if __name__ == "__main__":

    # for k in range(150):
    #     for i in range(3):
    send_event(producer, topic, after_elastic_data)
