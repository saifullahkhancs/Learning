import json


# Open the file and load its content
with open("t&te.json", "r") as json_file:
    data = json.load(json_file)

# Access the parsed JSON data
tactics = []
total_techniques  = data["techniques"]
total_sub_techniques = data["sub_techniques"]
for i in data["tactics"]:
    tactic = {"mitre_id": i.get("mitre_id") , "name": i.get("name") , "techniques_display_count" : 0, "display" : False}
    techniques = []
    # raltions = data["relationships"]

    filtered_relationships = [
    relationship for relationship in data["relationships"]
    if relationship["tactic_mitre_id"] == tactic["mitre_id"] and "." not in relationship["technique_mitre_id"]]
    tech_count = 0
    for rel in filtered_relationships:
        tech = next((tech for tech in total_techniques if  tech["mitre_id"] == rel["technique_mitre_id"]),None)
        if tech:
            print(f"Tactic: {tactic['name']} ({tactic['mitre_id']}) -> Technique: {tech['name']} ({tech['mitre_id']})")
            tech = ({"mitre_id": tech.get("mitre_id") , "name": tech.get("name") , "display" : False})

            tech_count += 1

            filtered_sub_relationships = [
                sub_relationship for sub_relationship in data["relationships"]
                if sub_relationship["tactic_mitre_id"] == tactic["mitre_id"] and "."  in sub_relationship["technique_mitre_id"] 
                and  sub_relationship["technique_mitre_id"].split(".")[0] == tech.get("mitre_id")
                ]
            sub_tech_count = 0 
            sub_techniques = []

            for sub_rel in filtered_sub_relationships:
                sub_tech = next((sub_tech for sub_tech in total_sub_techniques if  sub_tech["mitre_id"] == sub_rel["technique_mitre_id"]),None)
                if sub_tech:
                    print(f"Technique: {tech['name']} ({tech['mitre_id']}) -> Sub_Technique: {sub_tech['name']} ({sub_tech['mitre_id']})")
                    sub_techniques.append({"mitre_id": sub_tech.get("mitre_id") , "name": sub_tech.get("name") , "display" : False})
                    sub_tech_count += 1
            print(len(sub_techniques))
            tech["sub_techniques_count"]  = sub_tech_count
            tech["sub_techniques"] = sub_techniques
            
            techniques.append(tech)

    tactic["techniques_count"] = tech_count
    tactic["techniques"] =techniques

    tactics.append(tactic)



with open("Mitre.json", "w") as outfile:
    json.dump(tactics, outfile, indent=4)

print("Data has been written to output.json")
