from neo4j import GraphDatabase
import csv
from neo4j.exceptions import ServiceUnavailable, AuthError
import sys
import os
import json
# Define your Neo4j connection credentials
NEO4J_URI = "bolt://localhost:7687"  # Change if your Neo4j instance is on a different port
USERNAME = "neo4j"  # Replace with your Neo4j username
PASSWORD = "saifkhan"  # Replace with your Neo4j password

driver = GraphDatabase.driver(NEO4J_URI, auth=(USERNAME, PASSWORD))

if len(sys.argv) < 3:
    print("Error: Please provide both 'data' and 'type' arguments.")
    print("Usage: python your_script.py <file> <type>")
    sys.exit(1)


file = sys.argv[1]
type = sys.argv[2]
print(file)
print(type)

node_name = (os.path.splitext(os.path.basename(file))[0]).upper()
print(f"Reading file: {node_name}")
try:
        with driver.session() as session:
            result = session.run("RETURN 'Neo4j connection successful!' AS message")
            message = result.single().get("message")
            print(message)
except AuthError:
        print("Authentication failed. Check your username and password.")
except ServiceUnavailable:
        print("Connection failed. Ensure Neo4j is running and the URI is correct.")
except Exception as e:
        print(f"An error occurred: {e}")

data_list = []
# with open(file, mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     # Iterate through each row in the CSV and convert it into a dictionary
#     for row in csv_reader:
#         # Append the dictionary row to the data_list
#         data_list.append(row)

with open(file, mode='r') as file:
        data_list = json.load(file)
try:
        if type == "node":
                with driver.session() as session:
                        query = f"""
                        UNWIND $data_list AS row
                        CALL apoc.create.node(['{node_name}'], row) YIELD node
                        RETURN node
                        """
                        session.run(query, data_list=data_list)

        else:
                with driver.session() as session:
                        cypher_query = f"""
                                UNWIND $data_list AS row
                                WITH row, toUpper(row.relation) AS relationType
                                CALL apoc.merge.node([row.source_label], {{id: toString(row.source_id)}}) YIELD node AS source
                                CALL apoc.merge.node([row.target_label], {{id: toString(row.target_id)}}) YIELD node AS target
                                CALL apoc.create.relationship(source, relationType, {{}} , target) YIELD rel
                                RETURN source, rel, target
                                """
                        session.run(cypher_query, data_list=data_list)
                                # Print results to verify
                        # for record in result:
                        #         print(record)     
except Exception as e:
        print(f"An error occurred: {e}")
finally:
    driver.close()
