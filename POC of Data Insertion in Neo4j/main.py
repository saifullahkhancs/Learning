import subprocess
import sys
import os
import time

# Start time

env = os.environ.copy()
# subprocess.run([sys.executable, "data_insertion.py" ])
start_time = time.time()
subprocess.run([sys.executable, "neo4j_insertion.py" , "Group.csv" ,"node"])
subprocess.run([sys.executable, "neo4j_insertion.py" , "Message.csv" ,"node"])
subprocess.run([sys.executable, "neo4j_insertion.py" , "Person.csv" ,"node"])
subprocess.run([sys.executable, "neo4j_insertion.py" , "User.csv" ,"node"])
end_time = time.time()

elapsed_time = end_time - start_time
start_time = time.time()
print(f"Time taken to run the nodes script: {elapsed_time:.2f} seconds")
subprocess.run([sys.executable, "neo4j_insertion.py" , "User_Group.csv" ,"type"])
subprocess.run([sys.executable, "neo4j_insertion.py" , "User_Message.csv" ,"type"])
subprocess.run([sys.executable, "neo4j_insertion.py" , "User_Person.csv" ,"type"])


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to run the  relation scripts: {elapsed_time:.2f} seconds")