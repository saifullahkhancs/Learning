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

file1 = sys.argv[1]
file = sys.argv[1]
type = sys.argv[2]
print(file1)
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
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            print(headers)
           
            if type == "node":
                        properties = "{"
                        for i in headers:
                                properties += f"{i}:row.{i}, "
                        properties_string = properties[:-2]
                        properties_string += "}"
                        print(properties_string)
                        query = f"""LOAD CSV WITH HEADERS FROM 'file:///{file1}' AS row
                                WITH  row
                                MERGE (a:{node_name} {properties_string})
                                """
                       
                        session.run(
                                query,
                        )
                        print(query)
            else:
                        cypher_query =f"""LOAD CSV WITH HEADERS FROM 'file:///{file1}' AS row
                                        WITH row, toUpper(row.relation) AS relationType
                                        CALL apoc.merge.node([row.source_label], {{id: toString(row.source_id)}}) YIELD node AS source
                                        CALL apoc.merge.node([row.target_label], {{id: toString(row.target_id)}}) YIELD node AS target
                                        CALL apoc.create.relationship(source, relationType, {{}}, target) YIELD rel
                                        RETURN source, rel, target"""
                        # Execute the Cypher query
                        session.run(cypher_query,).consume()     
                        print(f"Executing query: {cypher_query}")      
        # driver.close()       
except Exception as e:
        print(f"An error occurred: {e}")
finally:
    driver.close()
