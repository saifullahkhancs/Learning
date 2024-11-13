import subprocess
import sys
import os
import time

# Start time

env = os.environ.copy()
# subprocess.run([sys.executable, "data_insertion.py" ])
start_time = time.time()
# subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "Group_v1.csv" ,"node"])
# subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "Message_v1.csv" ,"node"])
# subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "Person_v1.csv" ,"node"])
# subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User_v1.csv" ,"node"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User_Group_v1.csv" ,"relation"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User_Message_v1.csv" ,"relation"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User_Person_v1.csv" ,"relation"])


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to run the script: {elapsed_time:.2f} seconds")