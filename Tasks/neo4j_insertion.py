from neo4j import GraphDatabase
import csv
from neo4j.exceptions import ServiceUnavailable, AuthError
import sys
import os
# Define your Neo4j connection credentials
NEO4J_URI = "bolt://localhost:7687"  # Change if your Neo4j instance is on a different port
USERNAME = "neo4j"  # Replace with your Neo4j username
PASSWORD = "saifkhan"  # Replace with your Neo4j password

# Initialize the driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(USERNAME, PASSWORD))

# Check if both arguments are provided
if len(sys.argv) < 3:
    print("Error: Please provide both 'file' and 'type' arguments.")
    print("Usage: python your_script.py <file> <type>")
    sys.exit(1)


file = sys.argv[1]
type = sys.argv[2]

# if type == "relation":
#         if len(sys.argv) < 3:
#                 print("Error: Please provide both Labels")
#                 print("Usage: python your_script.py <file> <label1> <label2> <relation>")
#         label1 = sys.argv[3]
#         label2 = sys.argv[4]
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


try:
    with driver.session() as session:
        with open(file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            headers = csv_reader.fieldnames
            if type == "node":
                for row in csv_reader:
                        properties = {header: row[header] for header in headers}
                        cypher_query = f"CREATE (p:{node_name} $properties)"
                        session.run(
                        cypher_query,
                        properties=properties
                        )
                        print(properties.values())
            else:
                for row in csv_reader:
                        source_label, source_id = row["source"].split("_")
                        target_label, target_id = row["target"].split("_")
                        # source_id=int(source_id)
                        # target_id=int(target_id) 
                        relationship_type = row["relation"].upper()
                        cypher_query = f"""
                                MATCH (source:{source_label} {{id:"{source_id}"}})
                                MATCH (target:{target_label} {{id:"{target_id}"}})
                                MERGE (source)-[r:{relationship_type.upper()}]->(target)
                                """
                        print(f"Executing query: {cypher_query}")
                        # Execute the Cypher query
                        rsp = session.run(
                                cypher_query,
                                source_label=source_label,
                                target_label=target_label,
                                source_id = source_id,
                                target_id = target_id,
                                relationship_type=relationship_type
                                )
                        
        
        driver.close()       

finally:
    driver.close()
