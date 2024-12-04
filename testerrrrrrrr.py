list =  ["green","yellow","red" ,"amber"]
sorted_dict = {"green" : 1 , "amber" : 2 , "yellow" : 3 , "red" :4  }
if len(list) == 1:
    tlp = list

sorted_colors = sorted(list, key=lambda color: sorted_dict[color])

print(sorted_colors)



ip_event = {
        "value": "45.86.74.243",
        "type": "ipv4",
        "confidence": "medium",
        "sources": [
            {
                "id": "26",
                "name": "rstcloud",
                "display_name": "RST Cloud",
                "url": "https://raw.githubusercontent.com/rstcloud/rstthreats/master/feeds/full/random100_ioc_ip_latest.json",
                "confidence": "medium",
                "type": "open_feed",
                "time": "2023-12-13T00:03:37.288355"
            }
        ],
        "score": 68,
        "verdict": "suspicious",
        "approved": False,
        "malwares": [
            {
                "reported_source": {
                    "name": "rstcloud",
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
                    "name": "rstcloud",
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
                    "name": "rstcloud",
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
                    "name": "rstcloud",
                    "reported_time": "2023-12-02T19:25:03.278393",
                    "confidence": "high",
                    "type": "open_feed",
                    "sr_reviewed": None
                },
                "threat_type": "phishing"
            }
        ],
        "tools": [
            {
                "reported_source": {
                    "sr_reviewed": None,
                    "confidence": "high",
                    "name": "rstcloud",
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
            "cobalt_strike",
            "malware"
        ],
        "first_seen": "2023-03-13T00:00:00.909823",
        "last_seen": "2023-12-10T00:00:00.746659",
        "raw": [
            {
                "RST_Cloud_IP": {
                    "ip": {
                        "v4": "45.86.74.243",
                        "num": 760630003
                    },
                    "ports": [
                        8080
                    ],
                    "fseen": 1678665600,
                    "lseen": 1702166400,
                    "collect": 1702252800,
                    "src": {
                        "name": [
                            "github_repos"
                        ],
                        "report": "https://github.com/stamparm/maltrail"
                    },
                    "tags": {
                        "str": [
                            "malware"
                        ],
                        "codes": [
                            10
                        ]
                    },
                    "asn": {
                        "num": 44477,
                        "firstip": {
                            "netv4": "45.86.74.0",
                            "num": 760629760
                        },
                        "lastip": {
                            "netv4": "45.86.79.255",
                            "num": 760631295
                        },
                        "cloud": "",
                        "domains": 55899,
                        "org": "",
                        "isp": "STARKINDUSTRIES"
                    },
                    "geo": {
                        "city": "Manila",
                        "country": "Philippines",
                        "region": "Metro Manila"
                    },
                    "related": {
                        "domains": []
                    },
                    "score": {
                        "total": 6,
                        "src": 68.04,
                        "tags": 0.89,
                        "frequency": 0.1
                    },
                    "fp": {
                        "alarm": "False",
                        "descr": ""
                    },
                    "threat": [
                        "cobalt_strike"
                    ],
                    "cve": [],
                    "industry": [],
                    "ttp": [],
                    "id": "90e8a60a-a026-30fc-9d4e-33f4f361ce5b",
                    "title": "RST Threat feed. IOC: 45.86.74.243",
                    "description": "IOC with tags: malware. Related threats: cobalt_strike"
                }
            }
        ],
        "analysis": {
            "status": [],
            "verdict": [
                {
                    "value": "suspicious",
                    "reported_source": {
                        "name": "rstcloud",
                        "reported_time": "2023-12-13T00:03:37.288491",
                        "confidence": "medium",
                        "type": "open_feed",
                        "sr_reviewed": False
                    }
                }
            ],
            "confidence": [
                {
                    "value": "medium",
                    "reported_source": {
                        "name": "rstcloud",
                        "reported_time": "2023-12-13T00:03:37.288537",
                        "confidence": "medium",
                        "type": "open_feed",
                        "sr_reviewed": False
                    }
                }
            ],
            "score": [
                {
                    "value": "68.04",
                    "reported_source": {
                        "name": "rstcloud",
                        "reported_time": "2023-12-13T00:03:37.288567",
                        "confidence": "medium",
                        "type": "open_feed",
                        "sr_reviewed": False
                    }
                }
            ]
        },
        "presence_index": {},
        "mitigation_rules": [],
        "first_crawled": "2023-12-13T00:03:37.288582",
        "last_crawled": "2023-12-13T00:03:37.288582",
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
        "infra_info": {},
        "location_info": {
            "continent_code": "NA",
            "continent_name": "North America",
            "country_code": "US",
            "country_name": "United States",
            "country_is_in_european_union": None,
            "city": "Los Angeles",
            "region": "",
            "region_code": "",
            "country_code_iso3": "",
            "country_capital": "",
            "country_tld": "",
            "postal": "90009",
            "latitude": 34.0544,
            "longitude": -118.244,
            "timezone": "America/Los_Angeles",
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
            "subnet": "45.86.64.0/20",
            "subnet_allocation_age": None,
            "subnet_allocation_date": "",
            "subnet_reputation": None,
            "subnet_reputation_score": None,
            "subnet_density": {}
        },
        "asn_info": {
            "asn": 35913,
            "asn_allocation_age": None,
            "asn_allocation_date": "",
            "asn_rank": None,
            "asn_rank_score": None,
            "asn_reputation": None,
            "asn_reputation_score": None,
            "asn_takedown_reputation": None,
            "asn_takedown_reputation_score": None,
            "asname": "DEDIPATH-LLC",
            "date": "",
            "density": None,
            "ips_in_asn": None,
            "ips_num_active": None,
            "ips_num_listed": None,
            "asn_reputation_explanation": {}
        },
        "open_ports": [
            {
                "port": 8080,
                "type": ""
            }
        ],
        "host": {
            "value": "45.86.74.243",
            "type": "ipv4",
            "category": "ip",
            "port": None
        },
        "content_serving": {},
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
        "communicating_files": [
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
        "associated_urls": [
            {
                "url": {
                    "value": "http://36.49.34.150:12225/.i"
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
            "name": "45.86.74.243",
            "epp_status": [],
            "emails": [
                "hostmaster@ripe.net",
                "abuse@ripe.net"
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
            "isp_name": "Stark Industries Solutions LTD",
            "country": "Philippines",
            "date": "2023-12-13T00:03:36.804675"
        },
        "artifact_validation": [
            {
                "benign": False,
                "whitelisted": False,
                "is_deployable": True,
                "date": "2023-12-13T00:03:37.288985",
                "compromised": False,
                "is_fp": False,
                "forcefully_malicious": None,
                "source": "whitelisting_service"
            }
        ]
    }

