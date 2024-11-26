import json


# Open the file and load its content
with open("t&te.json", "r") as json_file:
    data = json.load(json_file)

# Access the parsed JSON data
tactics = []
total_techniques  = data["techniques"]
total_tactics = data["tactics"]
responce = {}
for tech in total_techniques:
    relative_tactics  = []
    filtered_relationships = [
    relationship for relationship in data["relationships"]
    if relationship["technique_mitre_id"] == tech["mitre_id"] and "." not in relationship["technique_mitre_id"]]
    tech_count = 0
    for rel in filtered_relationships:
        relative_tactics.append(rel["tactic_mitre_id"])

    responce[tech["mitre_id"]] = relative_tactics
    
with open("Techniques_With_Relative_Tactics.json", "w") as outfile:
    json.dump(responce, outfile, indent=4)