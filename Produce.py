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
    "score": 100,
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
    "first_seen": 1734436800.0,
    "last_seen":1734436800.0,
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
    "tlp": "RED",
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

object_event21  = {
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
    "score": 700,
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
    "first_seen": 1734264000.0,  
    "last_seen": 1734264000.0,
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
    "tlp": "amber",
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
    "md5": "",
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


object_event22  = {
  "meta": {
    "ver": 1.0,
    "_id": "2e6c4e66498be17f113e8d050d8e7acc61649aab",
    "index": "ver_1.0.1_strikeready_intel_14_object"
  },
  "data": {
    "value": "e56093a7cd414f5592cc76a41ddd4c25",
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
    "tags": ["i am in the new one"],
    "internal_tags": [
      "ua-wget",
      "malware_download",
      "elf",
      "mirai"
    ],
    "first_seen": 1734350400.0,
    "last_seen": 1734350400.0,
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
    "sha256": "",
    "sha512": "e56093a7cd414f5592cc76a41ddd4c25",
    "sha1": "",
    "sha3_384": "",
    "md5": "",
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




url_event2 = {
  'meta': {
    'ver': 1.0,
    '_id': 'd61051bdff4e3d17d0a031efa802d89628d47eb0',
    'index': 'ver_1.0.1_strikeready_intel_14_url'
  },
  'data': {
    'value': 'http://www.165-22-240-41.cprapid.com/ppc',
    'type': 'url',
    'confidence': 'high',
    'sources': [
      {
        'id': '29',
        'name': 'urlhaus',
        'display_name': 'URLhaus',
        'url': 'https://urlhaus-api.abuse.ch/v1/urls/recent/',
        'confidence': 'high',
        'type': 'ThreatFeed',
        'time': 1733448229.765526
      }
    ],
    'score': 90,
    'verdict': 'malicious',
    'approved': False,
    'malwares': [],
    'vulnerability': [],
    'threat_actors': [],
    'threat': [],
    'tools': [],
    'ransoms': [],
    'strikes': [],
    'tags': ["i am the new_one"],
    'internal_tags': ['ua-wget', 'malware_download', 'elf', 'mirai'],
    'first_seen': 1733420401.4,
    'last_seen': 1733420401.4,
    'raw': [
      {
        'urlhaus': {
          'id': 3331973,
          'urlhaus_reference': 'https://urlhaus.abuse.ch/url/3331973/',
          'url': 'http://www.165-22-240-41.cprapid.com/ppc',
          'url_status': 'offline',
          'host': 'www.165-22-240-41.cprapid.com',
          'date_added': '2024-12-05 17:40:14 UTC',
          'threat': 'malware_download',
          'blacklists': {
            'spamhaus_dbl': 'abused_legit_phishing',
            'surbl': 'listed'
          },
          'reporter': 'anonymous',
          'larted': 'True',
          'tags': ['elf', 'mirai', 'ua-wget']
        }
      }
    ],
    'presence_index': {},
    'mitigation_rules': [],
    'first_crawled': 1733448229.765881,
    'last_crawled': 1733448229.765883,
    'mitre_ttp': [],
    'tlp': 'white',
    'whitelisted_check': True,
    'internal_raw_osint': False,
    'internal_allow_sync': True,
    'associated_threat_campaigns': [],
    'is_deployable': True,
    'dark_feed': False,
    'sr_intel': False,
    'status': 'offline',
    'uri': '/ppc',
    'host': {
      'value': 'www.165-22-240-41.cprapid.com',
      'type': 'domain',
      'category': 'subdomain',
      'port': None
    },
    'larted': True,
    'open_ports': [],
    'files_downloaded': [
      {
        'object': {
          'sha256': 'f63279ee428bd0ae7ae9cbcbe3f6c16e1ae63d37dc7731c2c94c388a7aaedefd',
          'sha512': '',
          'sha1': '',
          'sha3_384': '',
          'md5': '',
          'tlsh': '',
          'telfhash': '',
          'ss_deep': '',
          'vhash': '',
          'imp_hash': '',
          'object_info': {
            'obj_uploaded_origin': '',
            'contacted_hosts': [],
            'contacted_urls': [],
            'downloaded_from_url': [],
            'downloaded_from_host': [],
            'files_opened': [],
            'files_deleted': [],
            'file_paths': [],
            'files_downloaded': [],
            'files_dropped': [],
            'files_written': [],
            'avs_detection': [],
            'file_size': None,
            'file_size_unit': '',
            'file_type': '',
            'file_extension': '',
            'associated_filenames': [],
            'packed': {}
          }
        }
      }
    ],
    'http_response': {
      'status_code': None,
      'response_len': None,
      'content_type': '',
      'filename': ''
    },
    'shortened': {
      'is_shorten': None,
      'final_location': {},
      'redirection_chain': []
    },
    'url_content_categorization': [],
    'urls_part_of_body': [],
    "url_whois": {
            "address": "",
            "city": "New-york",
            "country": "Pakistan",
            "state": "",
            "reverse_dns": [],
            },
    'artifact_validation': [
      {
        'benign': False,
        'whitelisted': False,
        'is_deployable': True,
        'domain_rank': None,
        'date': 1733448236.118214,
        'compromised': False,
        'is_fp': False,
        'forcefully_malicious': None,
        'source': 'whitelisting_service'
      }
    ]
  }
}


ip_event2 = {
  "meta": {
    "ver": 1.0,
    "_id": "12dfeb456c538f73cc2344fa3b8a161c5b34b54a",
    "index": "ver_1.0.1_strikeready_intel_14_ip"
  },
  "data": {
    "value": "59.182.145.194",
    "type": "ipv4",
    "confidence": "low",
    "sources": [
      {
        "id": "33",
        "name": "strikeready_research",
        "display_name": "Strikeready Research",
        "url": "",
        "confidence": "low",
        "type": "Derived_Intel",
        "time": 1733458853.201214
      }
    ],
    "score": 60,
    "verdict": "suspicious",
    "approved": False,
    "malwares": [
      {
        "value": "Mozi",
        "reported_source": {
          "name": "strikeready_research",
          "confidence": "high",
          "type": "ThreatResearch",
          "sr_reviewed": True,
          "reported_time": 1733458812.149448
        }
      }
    ],
    "vulnerability": [],
    "threat_actors": [],
    "threat": [],
    "tools": [],
    "ransoms": [],
    "strikes": [],
    "tags": ["mozi", "elf", "mips", "32-bit"],
    "internal_tags": ["elf", "mips", "32-bit", "mozi", "malware_download"],
    "first_seen": 1733458561.8,
    "last_seen": 1733458561.8,
    "raw": [
      {
        "urlhaus": {
          "id": 3332473,
          "urlhaus_reference": "https://urlhaus.abuse.ch/url/3332473/",
          "url": "http://59.182.145.194:39125/bin.sh",
          "url_status": "online",
          "host": "59.182.145.194",
          "date_added": "2024-12-06 04:16:18 UTC",
          "threat": "malware_download",
          "blacklists": {
            "spamhaus_dbl": "not listed",
            "surbl": "not listed"
          },
          "reporter": "geenensp",
          "larted": "True",
          "tags": ["32-bit", "elf", "mips", "Mozi"]
        }
      }
    ],
    "presence_index": {},
    "mitigation_rules": [],
    "first_crawled": 1733458853.201383,
    "last_crawled": 1733458853.201385,
    "mitre_ttp": [],
    "tlp": "white",
    "whitelisted_check": True,
    "internal_raw_osint": False,
    "internal_allow_sync": True,
    "associated_threat_campaigns": [],
    "is_deployable": True,
    "dark_feed": False,
    "sr_intel": False,
    "status": "",
    "infra_info": {
      "dnsbl_info": None,
      "reputation_info": None,
      "rDNS": None
    },
    "location_info": {
      "continent_code": "AS",
      "continent_name": "Asia",
      "country_code": "IN",
      "country_name": "India",
      "country_is_in_european_union": None,
      "city": "Thiruvananthapuram",
      "region": "",
      "region_code": "",
      "country_code_iso3": "",
      "country_capital": "",
      "country_tld": "",
      "postal": "695025",
      "latitude": 8.4832,
      "longitude": 76.9458,
      "timezone": "Asia/Kolkata",
      "utc_offset": "",
      "country_calling_code": "",
      "currency": "",
      "currency_name": "",
      "languages": [],
      "country_area": None,
      "country_population": None
    },
    "ip_type": "public",
    "ip_class": "A",
    "ip_history": [],
    "infra_security": {},
    "os_fingerprinting": {},
    "subnet_info": {
      "subnet": "59.182.0.0/15",
      "subnet_allocation_age": None,
      "subnet_allocation_date": "",
      "subnet_reputation": None,
      "subnet_reputation_score": None,
      "subnet_density": {}
    },
    "asn_info": {
      "asn": 9829,
      "asn_allocation_age": None,
      "asn_allocation_date": "",
      "asn_rank": None,
      "asn_rank_score": None,
      "asn_reputation": None,
      "asn_reputation_score": None,
      "asn_takedown_reputation": None,
      "asn_takedown_reputation_score": None,
      "asname": "National Internet Backbone",
      "date": "",
      "density": None,
      "ips_in_asn": None,
      "ips_num_active": None,
      "ips_num_listed": None,
      "asn_reputation_explanation": {}
    },
    "open_ports": [
      {
        "port": 39125,
        "type": ""
      }
    ],
    "host": {
      "value": "59.182.145.194",
      "type": "ipv4",
      "category": "ip",
      "port": None
    },
    "content_serving": {},
    "files_downloaded": [
      {
        "object": {
          "sha256": "4293c1d8574dc87c58360d6bac3daa182f64f7785c9d41da5e0741d2b1817fc7",
          "sha512": "",
          "sha1": "",
          "sha3_384": "",
          "md5": "",
          "tlsh": "",
          "telfhash": "",
          "ss_deep": "",
          "vhash": "",
          "imp_hash": "",
          "object_info": {
            "obj_uploaded_origin": "",
            "contacted_hosts": [],
            "contacted_urls": [],
            "downloaded_from_url": [],
            "downloaded_from_host": [],
            "files_opened": [],
            "files_deleted": [],
            "file_paths": [],
            "files_downloaded": [],
            "files_dropped": [],
            "files_written": [],
            "avs_detection": [],
            "file_size": None,
            "file_size_unit": "",
            "file_type": "",
            "file_extension": "",
            "associated_filenames": [],
            "packed": {}
          }
        }
      }
    ],
    "communicating_files": [],
    "associated_urls": [
      {
        "url": {
          "value": "http://59.182.145.194:39125/bin.sh"
        }
      }
    ],
    "ip_whois": {
      "address": "",
      "city": "",
      "country": "",
      "state": "",
      "reverse_dns": [],
      "creation_date": None,
      "expiration_date": None,
      "name": "59.182.145.194",
      "epp_status": ["allocated"],
      "emails": [
        "search-apnic-not-arin@apnic.net",
        "'abusemtnl@bol.net.in",
        "dgmitco@bol.net.in",
        "abusemtnl@bol.net.in",
        "mgritco@bol.net.in",
        "hostmaster@bsnl.co.in"
      ],
      "whois_server": "",
      "zip_code": None,
      "name_servers": [],
      "organization": "",
      "registrar": {
        "Registrar_WHOIS_Server": "",
        "Registrar_url": "",
        "Registrar_name": "",
        "Registrar_organization": "",
        "Registrar_location": {},
        "Registrar_status": "",
        "Registrar_IANA_id": ""
      },
      "referral_url": "",
      "dnssec": [],
      "registry_domain_url_id": "",
      "updated_at": None
    },
    "isp": {
      "isp_name": "AS9829 National Internet Backbone",
      "country": "IN",
      "date": 1733458853.300508
    },
    "artifact_validation": [
      {
        "benign": False,
        "whitelisted": False,
        "is_deployable": True,
        "date": 1733458853.864264,
        "compromised": False,
        "is_fp": False,
        "forcefully_malicious": None,
        "source": "whitelisting_service"
      }
    ]
  }
}


domain_event2 = {
    'meta': {
        'ver': 1.0,
        '_id': '8ce86cbc1fea90526058c67d30e645d06670658e',
        'index': 'ver_1.0.1_strikeready_intel_14_domain'
    },
    'data': {
        'value': 'www.stipamana.com',
        'type': 'domain',
        'confidence': 'high',
        'sources': [
            {
                'id': '27',
                'name': 'threat_fox',
                'display_name': 'Threat Fox',
                'url': 'https://threatfox-api.abuse.ch/api/v1/',
                'confidence': 'high',
                'type': 'ThreatFeed',
                'time': 1733465430.074513
            }
        ],
        'score': 75,
        'verdict': 'malicious',
        'approved': False,
        'malwares': [],
        'vulnerability': [],
        'threat_actors': [],
        'threat': [],
        'tools': [],
        'ransoms': [],
        'strikes': [],
        'tags': [ 
            "i am first one"
        ],
        'internal_tags': [
            'infostealer',
            'stealer',
            'lokibot',
            'loki password stealer (pws)',
            'lokipws',
            'loki',
            'burkina',
            'win.lokipws',
            'botnet_cc',
            "i"
        ],
        'first_seen':1734164925.335116,
        'last_seen': 1734078525.335116,
        'raw': [
            {
                'threat_fox': {
                    'id': '1352120',
                    'ioc': 'www.stipamana.com',
                    'threat_type': 'botnet_cc',
                    'threat_type_desc': 'Indicator that identifies a botnet command&control server (C&C)',
                    'ioc_type': 'domain',
                    'ioc_type_desc': 'Domain that is used for botnet Command&control (C&C)',
                    'malware': 'win.lokipws',
                    'malware_printable': 'Loki Password Stealer (PWS)',
                    'malware_alias': 'Burkina,Loki,LokiBot,LokiPWS',
                    'malware_malpedia': 'https://malpedia.caad.fkie.fraunhofer.de/details/win.lokipws',
                    'confidence_level': 75,
                    'first_seen': '2024-12-04 13:05:17 UTC',
                    'last_seen': '2024-12-06 06:00:04 UTC',
                    'reference': None,
                    'reporter': 'SarlackLab',
                    'tags': ['infostealer', 'LokiBot', 'stealer']
                }
            }
        ],
        'presence_index': {},
        'mitigation_rules': [],
        'first_crawled': 1733465430.074873,
        'last_crawled': 1733465430.074876,
        'mitre_ttp': [],
        'tlp': 'white',
        'whitelisted_check': True,
        'internal_raw_osint': False,
        'internal_allow_sync': True,
        'associated_threat_campaigns': [],
        'is_deployable': True,
        'dark_feed': False,
        'sr_intel': False,
        'dga_info': {
            'domain_string_frequency_probability': None
        },
        'domain_reputation': [],
        'infrastructure_info': {
            'cousin_domains': None,
            'resolving_ip': None,
            'dnsbl_info': None,
            'infra_tag': None,
            'mx_info': None,
            'ns_reputation': None,
            'sibling_domains': None
        },
        'status': '',
        'files_downloaded': [],
        'child_urls': [],
        'communicating_files': [],
        'passive_dns': [],
        'typosquat_info': {},
        'idn_info': {
            'is_idn': False,
            'punycode': ''
        },
        'tld_info': {
            'value': '.com'
        },
        'open_ports': [],
        'host': {
            'value': 'www.stipamana.com',
            'type': 'domain',
            'category': 'subdomain',
            'port': None
        },
        'ssl_certificate': {
            'host_name': None,
            'common_name': None,
            'san': None,
            'issuer': {},
            'not_before': None,
            'not_after': None,
            'certificate_authority': None,
            'md5_fingerprint': None,
            'sha1_fingerprint': None,
            'sha256_fingerprint': None,
            'cert_as_text': None,
            'revoked_status': None
        },
        'hierarchical_dns_analysis': {},
        'passive_content_analysis': {},
        'domain_whois': {
            'address': '',
            'city': '',
            'country': '',
            'state': '',
            'domain': 'www.stipamana.com',
            'creation_date': '2024-11-30 09:18:04.100000',
            'expiration_date': '2025-11-30 09:18:04.100000',
            'name': 'www.stipamana.com',
            'epp_status': ['clienttransferprohibited'],
            'emails': ['abuse@namecheap.com'],
            'whois_server': 'whois.namecheap.com',
            'zip_code': None,
            'name_servers': [
                'PDNS1.REGISTRAR-SERVERS.COM',
                'PDNS2.REGISTRAR-SERVERS.COM'
            ],
            'organization': '',
            'registrar': {
                'Registrar_WHOIS_Server': 'whois.namecheap.com',
                'Registrar_url': '',
                'Registrar_name': 'NameCheap, Inc.',
                'Registrar_organization': '',
                'Registrar_location': {},
                'Registrar_status': '',
                'Registrar_IANA_id': ''
            },
            'dnssec': ['unsigned'],
            'updated_at': '2024-11-30 09:18:04.300000'
        },
        'artifact_validation': [
            {
                'benign': False,
                'whitelisted': False,
                'is_deployable': True,
                'domain_rank': None,
                'date': 1733465440.627018,
                'compromised': False,
                'is_fp': False,
                'forcefully_malicious': None,
                'source': 'whitelisting_service'
            }
        ]
    }
}




topic  = "elastic"
# topic= "registered_user_thre"
if __name__ == "__main__":

    # for k in range(150):
    #     for i in range(3):
    registered_user = object
    response = producer.send(topic,object_event21 )
    print(response.get())
    time.sleep(5)
