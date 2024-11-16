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


file1 = sys.argv[1]
file2 = sys.argv[1]
type = sys.argv[2]
print(file1)
print(type)

node_name1 = (os.path.splitext(os.path.basename(file1))[0]).upper()
print(f"Reading file: {node_name1}")

node_name2 = (os.path.splitext(os.path.basename(file2))[0]).upper()
print(f"Reading file: {node_name2}")

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

with open(file1, mode='r') as file1:
        data_list1 = json.load(file1)
with open(file2, mode='r') as file2:
        data_list2 = json.load(file2)
try:
        csv_reader1 = csv.reader(file1)
        headers1 = next(csv_reader1)
        print(headers1)
        csv_reader2 = csv.reader(file2)
        headers2 = next(csv_reader2)
        print(headers2)
        if type == "node":
                with driver.session() as session:
                        properties1 = "{"
                        for i in headers1:
                                properties1 += f"{i}:row.{i}, "
                        properties_string1 = properties1[:-2]
                        properties_string1 += "}"
                        print(properties_string1)

                        properties2 = "{"
                        for i in headers2:
                                properties2 += f"{i}:row.{i}, "
                        properties_string2 = properties2[:-2]
                        properties_string2 += "}"
                        print(properties_string2)
                        query = f"""
                                LOAD CSV WITH HEADERS FROM 'file:///C:/Learning/Task2/{file1}' AS row
                                WITH  row
                                MERGE (a:{node_name1} {properties_string1})
                                LOAD CSV WITH HEADERS FROM 'file:///C:/Learning/Task2/{file2}' AS row
                                WITH  row
                                MERGE (a:{node_name2} {properties_string2})

                                """
                        # query = f"""
                        #         UNWIND $data_list1 AS row
                        #         CALL apoc.merge.node(['{node_name1}'], row) YIELD node
                        #         RETURN node
                        #         UNWIND $data_list2 AS row
                        #         CALL apoc.merge.node(['{node_name2}'], row) YIELD node
                        #         RETURN node
                        # """
                        session.run(query, data_list1=data_list1 ,  data_list2=data_list2)

        else:
                with driver.session() as session:
                        cypher_query = f"""
                                UNWIND $data_list AS row
                                WITH row, toUpper(row.relation) AS relationType
                                CALL apoc.merge.node([row.source_label], {{id: toString(row.source_id)}}) YIELD node AS source
                                CALL apoc.merge.node([row.target_label], {{id: toString(row.target_id)}}) YIELD node AS target
                                CALL apoc.merge.relationship(source, relationType, {{id: row.id}}, {{}}, target) YIELD rel
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
