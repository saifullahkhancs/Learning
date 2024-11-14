import subprocess
import sys
import os
import time
import csv
import json

# Start time

env = os.environ.copy()
# subprocess.run([sys.executable, "data_insertion.py" ])


def preprocess_csv(input_file, output_file):
    data_list = []
    with open(input_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # You can modify the data here if needed, e.g., converting values or adding fields
            data_list.append(row)

    # Save the data list to a new JSON file or CSV
    with open(output_file, mode='w') as json_file:
        json.dump(data_list, json_file)

# Preprocess and save the file
# Convert each CSV to JSON
input_file = "Group.csv"
output_file = "Group.json"
preprocess_csv(input_file, output_file)

input_file = "Message.csv"
output_file = "Message.json"
preprocess_csv(input_file, output_file)

input_file = "Person.csv"
output_file = "Person.json"
preprocess_csv(input_file, output_file)

input_file = "User.csv"
output_file = "User.json"
preprocess_csv(input_file, output_file)

input_file = "User_Group.csv"
output_file = "User_Group.json"
preprocess_csv(input_file, output_file)

input_file = "User_Message.csv"
output_file = "User_Message.json"
preprocess_csv(input_file, output_file)

input_file = "User_Person.csv"
output_file = "User_Person.json"
preprocess_csv(input_file, output_file)

# Execute insertion scripts for each JSON file
start_time = time.time()
subprocess.run([sys.executable, "neo4j_insertion_v2.py", "Group.json", "node"])
subprocess.run([sys.executable, "neo4j_insertion_v2.py", "Message.json", "node"])
subprocess.run([sys.executable, "neo4j_insertion_v2.py", "Person.json", "node"])
subprocess.run([sys.executable, "neo4j_insertion_v2.py", "User.json", "node"])
subprocess.run([sys.executable, "neo4j_insertion_v2.py", "User_Group.json", "type"])
subprocess.run([sys.executable, "neo4j_insertion_v2.py", "User_Message.json", "type"])
subprocess.run([sys.executable, "neo4j_insertion_v2.py", "User_Person.json", "type"])



end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to run the script: {elapsed_time:.2f} seconds")