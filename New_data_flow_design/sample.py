url_event =  {
    "value": "https://vk.com/doc418490229_669356461?hash=QZ4Z4X5d1YyJIYsuybrCPLzO6Ls2spy0JgNSqnc72tL&dl=0LhPUEBSvCJyNIPscRw3GxYsokIzwdbZxqgmCthcoz8&api=1&no_preview=1#xin",
    "type": "url",
    "confidence": "high",
    "sources": [
      {
        "id": "29",
        "name": "urlhaus",
        "display_name": "Urlhaus",
        "url": "https://urlhaus-api.abuse.ch/v1/urls/recent/",
        "confidence": "high",
        "type": "open_feed",
        "time": "2023-12-08T22:01:18.585919"
      }
    ],
    "score": 90,
    "verdict": "malicious",
    "approved": False,
    "malwares": [
      {
        "reported_source": {
          "name": "urlhaus",
          "sr_reviewed": None,
          "reported_time": "2024-01-07T11:31:21.220030",
          "type": "open_feed",
          "confidence": "high"
        },
        "value": "Redline Stealer"
      }
    ],
    "vulnerability": [
      {
        "value": "Follina",
        "reported_cves": "CVE-2022-0732",
        "reported_source": {
          "name": "urlhaus",
          "reported_time": "2024-02-15T21:21:30.153664",
          "confidence": "low",
          "type": "open_feed",
          "sr_reviewed": None
        }
      }
    ],
    "threat_actors": [
      {
        "value": "LV Ransomware Group",
        "reported_source": {
          "name": "urlhaus",
          "reported_time": "2023-03-29T11:36:56.951523",
          "confidence": "high",
          "type": "open_feed",
          "sr_reviewed": None
        }
      }
    ],
    "threat": [
      {
        "stage": "",
        "reported_source": {
          "name": "urlhaus",
          "reported_time": "2023-12-08T22:01:18.585985",
          "confidence": "high",
          "type": "open_feed",
          "sr_reviewed": None
        },
        "threat_type": "malware_download"
      }
    ],
    "tools": [
      {
        "reported_source": {
          "sr_reviewed": None,
          "confidence": "high",
          "name": "urlhaus",
          "reported_time": "2023-12-02T15:10:33.417572",
          "type": "open_feed"
        },
        "value": "Beacon"
      }
    ],
    "strikes": [
      "STA4090"
    ],
    "tags": [
      "encrypted",
      "dropped-by-PrivateLoader"
    ],
    "first_seen": "2023-12-08T21:50:03.600000",
    "last_seen": "2023-12-08T21:50:03.600000",
    "raw": [
      {
        "urlhaus": {
          "id": 2738929,
          "urlhaus_reference": "https://urlhaus.abuse.ch/url/2738929/",
          "url": "https://vk.com/doc418490229_669356461?hash=QZ4Z4X5d1YyJIYsuybrCPLzO6Ls2spy0JgNSqnc72tL&dl=0LhPUEBSvCJyNIPscRw3GxYsokIzwdbZxqgmCthcoz8&api=1&no_preview=1#xin",
          "url_status": "offline",
          "host": "vk.com",
          "date_added": "2023-12-08 21:50:36 UTC",
          "threat": "malware_download",
          "blacklists": {
            "spamhaus_dbl": "not listed",
            "surbl": "not listed"
          },
          "reporter": "andretavare5",
          "larted": "False",
          "tags": [
            "dropped-by-PrivateLoader",
            "encrypted"
          ]
        }
      }
    ],
    "analysis": {
      "status": [
        {
          "reported_source": {
            "name": "urlhaus",
            "sr_reviewed": False,
            "reported_time": "2023-12-08T22:01:18.586065",
            "type": "open_feed",
            "confidence": "high"
          },
          "value": "offline"
        }
      ],
      "verdict": [
        {
          "reported_source": {
            "name": "urlhaus",
            "sr_reviewed": True,
            "reported_time": "2023-12-08T22:01:18.586092",
            "type": "open_feed",
            "confidence": "high"
          },
          "value": "malicious"
        }
      ],
      "confidence": [
        {
          "reported_source": {
            "name": "urlhaus",
            "sr_reviewed": True,
            "reported_time": "2023-12-08T22:01:18.586116",
            "type": "open_feed",
            "confidence": "high"
          },
          "value": "high"
        }
      ],
      "score": [
        {
          "reported_source": {
            "name": "urlhaus",
            "sr_reviewed": True,
            "reported_time": "2023-12-08T22:01:18.586142",
            "type": "open_feed",
            "confidence": "high"
          },
          "value": "90"
        }
      ]
    },
    "presence_index": {},
    "mitigation_rules": [],
    "first_crawled": "2023-12-08T22:01:18.586156",
    "last_crawled": "2023-12-08T22:01:18.586157",
    "mitre_ttp": [
      {
        "tac_id": "TA0008",
        "tac_name": "Lateral Movement",
        "tech": [
          {
            "tech_id": "T1550",
            "tech_name": "Privilege Escalation",
            "sub_tech": [
              {
                "sub_tech_id": ".002",
                "sub_tech_name": "Powershell"
              }
            ]
          }
        ]
      }
    ],
    "tlp": "green",
    "whitelisted_check": True,
    "internal_raw_osint": False,
    "internal_allow_sync": True,
    "associated_threat_campaigns": [
      {
        "campaign_name": "Google Breach",
        "attack_origin": [
          "Russia"
        ],
        "targeted_region": [
          "North America"
        ],
        "sources": [
          {
            "confidence": "medium",
            "name": "open_phish",
            "id": "10",
            "time": "2023-12-25T08:50:27.882234",
            "display_name": "OpenPhish",
            "type": "open_feed",
            "url": "https://www.openphish.com/"
          }
        ],
        "targeted_country": [
          "us"
        ],
        "targeted_industry": [
          "Finance"
        ],
        "target": "AT&T Inc.",
        "targeted_sector": [
          "Finance"
        ]
      }
    ],
    "status": "offline",
    "uri": "/doc418490229_669356461hash=QZ4Z4X5d1YyJIYsuybrCPLzO6Ls2spy0JgNSqnc72tL&dl=0LhPUEBSvCJyNIPscRw3GxYsokIzwdbZxqgmCthcoz8&api=1&no_preview=1xin",
    "host": {
      "type": "domain",
      "category": "domain",
      "port": None,
      "value": "vk.com"
    },
    "larted": False,
    "open_ports": [
      {
        "port": 39901,
        "type": ""
      }
    ],
    "files_downloaded": [
      {
        "object": {
          "sha1": "",
          "sha256": "283c4f9174d19944189f5d6961f3319420c752bfaa6f65c19dd85ad2ca1cd77f",
          "object_info": {},
          "sha3_384": "",
          "ss_deep": "",
          "sha512": "",
          "tlsh": "",
          "vhash": "",
          "imp_hash": "",
          "telfhash": "",
          "md5": ""
        }
      }
    ],
    "http_response": {},
    "shortened": {
      "redirection_chain": [
        {
          "url": {
            "value": "http://bafybeihvi5l7repjrrhs6y677rs2ocbbkohwumgtykbxn7let326dgurne.ipfs.dweb.link/"
          }
        }
      ],
      "is_shorten": False,
      "final_location": {
        "url": {
          "value": "https://vk.com/doc418490229_669356461?hash=QZ4Z4X5d1YyJIYsuybrCPLzO6Ls2spy0JgNSqnc72tL&dl=0LhPUEBSvCJyNIPscRw3GxYsokIzwdbZxqgmCthcoz8&api=1&no_preview=1#xin"
        }
      }
    },
    "url_content_categorization": [],
    "urls_part_of_body": [],
    "phishing_info": {},
    "artifact_validation": [
      {
        "benign": False,
        "whitelisted": False,
        "is_deployable": True,
        "domain_rank": None,
        "date": "2023-12-08T22:01:18.586266",
        "compromised": False,
        "is_fp": False,
        "forcefully_malicious": None,
        "source": "whitelisting_service"
      }
    ],
    "is_fp": None
  }


