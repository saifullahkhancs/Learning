{
	"meta": 
    {
        "timestamp": 1690206793348, "username": "neo4j", "txId":
		122286186,
			 "txEventId": 2, "txEventsCount": 51, "operation": "updated",
			 "source": {"hostname": "neo4j-cluster-core-1"}
    },

	"payload": 
    {
        "id": "2416675", 
        "before": 
        {
		    "properties": {"date": "September 26, 2022",
					   "ransomwareExtension": [".mallox", ".FARGO", ".FARGO02",
											   ".FARGO03", ".FARGO04"],
					    "description": "FARGO is a ransomware that targets "
									  "vulnerable MS-SQL servers. Along with "
									  "GlobeImposter, FARGO is one of the "
									  "prominent ransomware that targets "
									  "vulnerable MS-SQL servers. In the "
									  "past, "
									  "it was also called the Mallox because "
									  "it used the file extension .mallox. It "
									  "does not infect files with a file "
									  "extension associated with "
									  "Globeimposter "
									  "and the exclusion list does not only "
									  "include the same type of extensions of "
									  ".FARGO .FARGO2 and .FARGO3 but also "
									  "includes .FARGO4, which is thought to "
									  "be a future version of the ransomware.",
					   "platform": "[\'windows\']",
					   "srid": "ransom-fargo-d3b5375a-9356-40a5-bdba"
							   "-8aa350bdfa14",
					   "uid": "d56276fa-c732-4bfe-8452-cfc31c99ca3c",
					   "extensions": [],
					   "refs": "[\'https://asec.ahnlab.com/en/39152/\']",
					   "name": "FARGOo",
					   "alias": "[\'FARGO\',\'Mallox\',\'TargetCompany\',"
								"\'Target Company\']",
					   "ransomNote": "[]"}, 
             "labels": ["Ransom"],
         },
                        
        "after": 
        {
		    "properties": {"date": "September 26, 2022",
					   "impHash": "f34d5f2d4577ed6d9ceec516c1f5a744",
					   "sha256":
						   "e5f20c03da31983648fca8c76f9be565e7d2fb13e2c5bc85da012d72e81dbf1c",
					   "ransomwareExtension": [".FARGO", ".mallox", ".FARGO02",
											   ".FARGO04", ".FARGO03"],
					   "vHash": "21403655551c0824c2010",
					   "description": "FARGO is a ransomware that targets "
									  "vulnerable MS-SQL servers. Along with "
									  "GlobeImposter, FARGO is one of the "
									  "prominent ransomware that targets "
									  "vulnerable MS-SQL servers. In the "
									  "past, "
									  "it was also called the Mallox because "
									  "it used the file extension .mallox. It "
									  "does not infect files with a file "
									  "extension associated with "
									  "Globeimposter "
									  "and the exclusion list does not only "
									  "include the same type of extensions of "
									  ".FARGO .FARGO2 and .FARGO3 but also "
									  "includes .FARGO4, which is thought to "
									  "be a future version of the ransomware.",
					   "platform": "[\'windows\']",
					   "srid": "ransom-fargo-d3b5375a-9356-40a5-bdba"
							   "-8aa350bdfa14",
					   "sha1": "e80210e52f244a929706032fde46e770f1912397",
					   "uid": "d56276fa-c732-4bfe-8452-cfc31c99ca3c",
					   "extensions": [],
					   "encryption": "ChaCha20, AES-128, Curve25519",
					   "refs": "[\'https://asec.ahnlab.com/en/39152/\',"
							   "\'https://thehackernews.com/2023/07/mallox"
							   "-ransomware-exploits-weak-ms-sql.html\',"
							   "\'https://malpedia.caad.fkie.fraunhofer.de"
							   "/details/win.targetcompany\']",
					   "name": "FARGO",
					   "alias": "[\'targetcompany\',\'target company\',"
								"\'mallox\',\'fargo\',\'Tohnichi\',"
								"\'Xollam\']",
					   "ransomNote": "[]", "_cms_": True,
					   "authentiHash":
						   "faed45f4fb4e38da8a9b3e4ba4d4ebcec6ec3ec166bd491064ea99139ffc9cb9",
					   "ssDeep":
						   "6144:aN3mSCFhYJWHXA"
						   "/r9q7DQjBe2OTix5WU5vso0nKqUSAjgDv1acP04xKWO0"
						   ":sJKGJf/I78L3LCoIKq1acVK",
					   "md5": "315aaf1f0128e50999fd5b82949a9267" 
                       
                    },
		    "labels": ["Ransom"],
        },
                     
        "type": "node"
        
    }, 

    "schema": 
    {
		"properties": 
        {
            "date": "String",
            "impHash": "String",
			"sha256": "String", 
            "ransomwareExtension": "String[]",
					"vHash": "String",
                      "description": "String",
					"platform": "String",
                      "srid": "String",
                        "sha1":"String",
					   "uid": "String", "extensions": "String[]",
					   "encryption": "String", "refs": "String",
					   "name": "String", "alias": "String",
					   "ransomNote": "String", "_cms_": "Boolean",
					   "authentiHash": "String", "ssDeep": "String",
					   "md5": "String"
        },

        "constraints": 
        [
			{"label": "Ransom", "properties": ["srid"], "type": "UNIQUE"},
			{"label": "Ransom", "properties": ["uid"], "type": "UNIQUE"}
        ]
    }
}
