list =  ["green","yellow","red" ,"amber"]
sorted_dict = {"green" : 1 , "amber" : 2 , "yellow" : 3 , "red" :4  }
if len(list) == 1:
    tlp = list

sorted_colors = sorted(list, key=lambda color: sorted_dict[color])

print(sorted_colors)


# new_sorted_dict ={}
# index = 0
# for i in list:
#     value = sorted_dict[i]
#     print(value)



{
    "meta": {
        "ver": 1
    },
    "data": {
        "value": "metamask.tokenim.ink",
        "type": "domain",
        "confidence": "high",
        "sources": [
            {
                "id": "12",
                "name": "phishtank",
                "display_name": "PhishTank",
                "url": "http://www.phishtank.com/phish_detail.php?phish_id=8376954",
                "confidence": "high",
                "type": "open_feed",
                "time": "2023-12-02T19:25:03.278296"
            }
        ],
        "score": 80,
        "verdict": "malicious",
        "approved": False,
        "malwares": [
            {
                "reported_source": {
                    "name": "phishtank",
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
                    "name": "phishtank",
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
                    "name": "phishtank",
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
                    "name": "phishtank",
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
                    "name": "phishtank",
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
            "cobalt_strike"
        ],
        "first_seen": "2023-11-27T21:58:03.600000",
        "last_seen": "2023-11-27T22:23:04.700000",
        "raw": [
            {
                "phishtank": {
                    "phish_id": 8376954,
                    "url": "http://metamask.tokenim.ink",
                    "phish_detail_url": "http://www.phishtank.com/phish_detail.php?phish_id=8376954",
                    "submission_time": "2023-11-27T21:58:36+00:00",
                    "verified": "yes",
                    "verification_time": "2023-11-27T22:23:47+00:00",
                    "online": "yes",
                    "details": [
                        {
                            "ip_address": "194.124.216.137",
                            "cidr_block": "194.124.216.0/24",
                            "announcing_network": "3214",
                            "rir": "ripencc",
                            "country": "DE",
                            "detail_time": "2023-11-27T22:13:29+00:00"
                        }
                    ],
                    "target": "Other"
                }
            }
        ],
        "analysis": {
            "status": [
                {
                    "value": "online",
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": "2023-12-02T19:25:03.278478",
                        "confidence": "high",
                        "type": "open_feed",
                        "sr_reviewed": False
                    }
                }
            ],
            "verdict": [
                {
                    "value": "malicious",
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": "2023-12-02T19:25:03.278517",
                        "confidence": "high",
                        "type": "open_feed",
                        "sr_reviewed": True
                    }
                }
            ],
            "confidence": [
                {
                    "value": "high",
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": "2023-12-02T19:25:03.278555",
                        "confidence": "high",
                        "type": "open_feed",
                        "sr_reviewed": True
                    }
                }
            ],
            "score": [
                {
                    "value": "80",
                    "reported_source": {
                        "name": "phishtank",
                        "reported_time": "2023-12-02T19:25:03.278603",
                        "confidence": "high",
                        "type": "open_feed",
                        "sr_reviewed": True
                    }
                }
            ]
        },
        "presence_index": {},
        "mitigation_rules": [],
        "first_crawled": "2023-12-02T19:25:03.806660",
        "last_crawled": "2023-12-02T19:25:03.806663",
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
        "dga_info": {},
        "domain_reputation": [],
        "infrastructure_info": {
            "cousin_domains": None,
            "resolving_ip": [
                {
                    "ip": {
                        "value": "194.124.216.137",
                        "time": "2023-12-02T19:25:03.278688"
                    }
                }
            ],
            "dnsbl_info": None,
            "infra_tag": None,
            "mx_info": None,
            "ns_reputation": None,
            "sibling_domains": None
        },
        "status": "online",
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
        "child_urls": [
            {
                "url": {
                    "value": "http://metamask.tokenim.ink"
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
        "passive_dns": [],
        "typosquat_info": {},
        "idn_info": {
            "is_idn": False,
            "punycode": ""
        },
        "tld_info": {
            "value": ".ink"
        },
        "open_ports": [
            {
                "port": 39901,
                "type": ""
            }
        ],
        "host": {
            "value": "metamask.tokenim.ink",
            "type": "domain",
            "category": "subdomain",
            "port": None
        },
        "ssl_certificate": {},
        "hierarchical_dns_analysis": {},
        "passive_content_analysis": {},
        "domain_whois": {
            "address": "REDACTED FOR PRIVACY",
            "city": "REDACTED FOR PRIVACY",
            "country": "CN",
            "state": "Guizhou",
            "domain": "metamask.tokenim.ink",
            "creation_date": "2023-09-26 17:23:00.100000",
            "expiration_date": "2024-09-26 17:23:00.100000",
            "name": "metamask.tokenim.ink",
            "epp_status": [
                "clientHold",
                "clientTransferProhibited",
                "clientTransferProhibited",
                "clientHold"
            ],
            "emails": [
                "kf@zzy.cn"
            ],
            "whois_server": "whois.zzy.cn",
            "zip_code": None,
            "name_servers": [
                "ns1.cnolnic.net",
                "ns2.cnolnic.net"
            ],
            "organization": "",
            "registrar": {
                "Registrar_WHOIS_Server": "whois.zzy.cn",
                "Registrar_url": "",
                "Registrar_name": "XIAMEN CHINASOURCE INTERNET SERVICE CO., LTD.",
                "Registrar_organization": "",
                "Registrar_location": {},
                "Registrar_status": "",
                "Registrar_IANA_id": ""
            },
            "dnssec": [
                "unsigned"
            ],
            "updated_at": "2023-11-28 01:12:04.400000"
        },
        "artifact_validation": [
            {
                "benign": False,
                "whitelisted": False,
                "is_deployable": True,
                "domain_rank": None,
                "date": "2023-12-02T19:25:03.278894",
                "compromised": False,
                "is_fp": False,
                "forcefully_malicious": None,
                "source": "whitelisting_service"
            }
        ]
    }
}


