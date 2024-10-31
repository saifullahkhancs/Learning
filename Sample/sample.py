tech_list =  [
          {
            "name": "exfiltration over other network medium",
            "mitreId": "T1011"
          },
          {
            "name": "Gather Victim Network Information",
            "mitreId": "T1590"
          },
          {
            "name": "Data Encrypted for Impact",
            "mitreId": "T1486"
          },
          {
            "name": "Transfer Data to Cloud Account",
            "mitreId": "T1537"
          },
          {
            "name": "System Network Configuration Discovery",
            "mitreId": "T1016"
          }
        ]

response_list = [
          {
            "name": "exfiltration over other network medium",
            "mitreId": "T1011"
          },
          {
            "name": "Gather Victim Network Information",
            "mitreId": "T1590"}
        ]

difference_list = [item for item in tech_list if item["mitreId"] not in {r["mitreId"] for r in response_list}]

print(difference_list)