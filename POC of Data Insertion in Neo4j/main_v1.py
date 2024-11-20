import subprocess
import sys
import os
import time

# Start time

env = os.environ.copy()
start_time = time.time()
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "Group.csv" ,"node"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "Message.csv" ,"node"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "Person.csv" ,"node"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User.csv" ,"node"])

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to run the nodes script: {elapsed_time:.2f} seconds")
start_time = time.time()
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User_Group.csv" ,"relation"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User_Message.csv" ,"relation"])
subprocess.run([sys.executable, "neo4j_insertion_v1.py" , "User_Person.csv" ,"relation"])


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to run the relation script: {elapsed_time:.2f} seconds")