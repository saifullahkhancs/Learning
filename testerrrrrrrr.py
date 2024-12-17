list =  ["green","yellow","red" ,"amber"]
sorted_dict = {"green" : 1 , "amber" : 2 , "yellow" : 3 , "red" :4  }
if len(list) == 1:
    tlp = list

sorted_colors = sorted(list, key=lambda color: sorted_dict[color])

print(sorted_colors)


object_event2  = {
  "meta": {
    "ver": 1.0,
    "_id": "2e6c4e66498be17f113e8d050d8e7acc61649aab",
    "index": "ver_1.0.1_strikeready_intel_14_object"
  },
  "data": {
    "value": "87039bdcf2482b1eee3aedb682d9a98cc0898a37f4004cfed0e508fad83c9d8a",
    "type": "object",
    "confidence": "low",
    "sources": [
      {
        "id": "29",
        "name": "urlhaus",
        "display_name": "URLhaus",
        "url": "https://urlhaus-api.abuse.ch/v1/urls/recent/",
        "confidence": "high",
        "type": "ThreatFeed",
        "time": 1733448255.905796
      }
    ],
    "score": 70,
    "verdict": "suspicious",
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
      "ua-wget",
      "malware_download",
      "elf",
      "mirai"
    ],
    "first_seen": 1733420401.4,
    "last_seen": 1733420401.4,
    "raw": [
      {
        "urlhaus": [
          {
            "firstseen": "2024-12-05",
            "filename": None,
            "file_type": "elf",
            "response_size": "108232",
            "response_md5": "e56093a7cd414f5592cc76a41ddd4c25",
            "response_sha256": "87039bdcf2482b1eee3aedb682d9a98cc0898a37f4004cfed0e508fad83c9d8a",
            "urlhaus_download": "https://urlhaus-api.abuse.ch/v1/download/87039bdcf2482b1eee3aedb682d9a98cc0898a37f4004cfed0e508fad83c9d8a/",
            "signature": "Mirai",
            "virustotal": None,
            "imphash": None,
            "ssdeep": "3072:VkNm/Hiw6xmycYt/hBxdVpYZP5Rhr/Z73O43p0:Vx/Cw6x5cYt/hbZ63qgp0",
            "tlsh": "T12BB36DD5E283D8F2D8271470603AD73BAF32D07A7219EA82C768DD31ACD1E41D627A"
          }
        ]
      }
    ],
    "presence_index": {},
    "mitigation_rules": [],
    "first_crawled": 1733448255.906131,
    "last_crawled": 1733448255.906134,
    "mitre_ttp": [],
    "tlp": "white",
    "whitelisted_check": True,
    "internal_raw_osint": False,
    "internal_allow_sync": True,
    "associated_threat_campaigns": [],
    "is_deployable": True,
    "dark_feed": False,
    "sr_intel": False,
    "sha256": "87039bdcf2482b1eee3aedb682d9a98cc0898a37f4004cfed0e508fad83c9d8a",
    "sha512": "",
    "sha1": "",
    "sha3_384": "",
    "md5": "e56093a7cd414f5592cc76a41ddd4c25",
    "tlsh": "t12bb36dd5e283d8f2d8271470603ad73baf32d07a7219ea82c768dd31acd1e41d627a",
    "telfhash": "",
    "ss_deep": "3072:VkNm/Hiw6xmycYt/hBxdVpYZP5Rhr/Z73O43p0:Vx/Cw6x5cYt/hbZ63qgp0",
    "vhash": "",
    "imp_hash": "",
    "artifact_validation": [
      {
        "benign": False,
        "whitelisted": False,
        "is_deployable": True,
        "file_owner": "",
        "date": 1733448256.108709,
        "compromised": False,
        "is_fp": False,
        "forcefully_malicious": None,
        "source": "whitelisting_service"
      }
    ],
    "object_info": {
      "obj_uploaded_origin": "",
      "contacted_hosts": [],
      "contacted_urls": [],
      "downloaded_from_url": [
        {
          "url": {
            "value": "http://www.165-22-240-41.cprapid.com/debug.dbg"
          }
        }
      ],
      "downloaded_from_host": [
        {
          "value": "www.165-22-240-41.cprapid.com",
          "type": "domain",
          "category": "subdomain",
          "port": None
        }
      ],
      "files_opened": [],
      "files_deleted": [],
      "file_paths": [],
      "files_downloaded": [],
      "files_dropped": [],
      "files_written": [],
      "avs_detection": [],
      "file_size": 108232,
      "file_size_unit": "",
      "file_type": "elf",
      "file_extension": ".elf",
      "associated_filenames": [],
      "packed": {
        "is_packed": None,
        "packer_type": None
      }
    }
  }
}
