import csv 
import random
import string
from datetime import datetime, timedelta
import uuid

countries = ["Nigeria", "USA", "Canada", "Brazil", "India", "Australia", "Germany", "France", "Japan", "South Africa"]
all_names = []
def generate_name():
    length = random.randint(3, 15)  # Generate random length between 3 and 8
    name = random.choice(string.ascii_uppercase)  # Start with a capital letter
    name += ''.join(random.choices(string.ascii_lowercase, k=length-1))  # Add random lowercase letters
    if name in all_names:
        generate_name()
    else:
        return name

def generate_message():
    length = random.randint(5, 15)  # Generate random length between 3 and 8
    message = random.choice(string.ascii_uppercase)  # Start with a capital letter
    message += ''.join(random.choices(string.ascii_lowercase, k=length-1))
    return message

def generate_random_datetime(start_date, month_duration=30):
    end_date = start_date + timedelta(days=month_duration)
    
    random_days = random.randint(0, month_duration)  # Random days within the month
    random_seconds = random.randint(0, 86400)  # Random seconds in a day (24 hours * 60 minutes * 60 seconds)
    random_datetime = start_date + timedelta(days=random_days, seconds=random_seconds)
    
    return random_datetime


def generate_id(IdList):
    id  = uuid.uuid4()
    if id in IdList or id == None:
        return generate_id(IdList)
    else:
        IdList.append(id)
        return id

with open("Person_v1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" ,"name", "age", "country"]
    writer.writerow(field)
    person_ids= []
    for i in range(20000):
        id = generate_id(person_ids)
        writer.writerow([id ,generate_name(), random.randint(18,60), random.choice(countries)])


roles = ["Manager" , "Assistant_Manger" , "Employee", "Worker", "Staff"]
grades = {"Manager": 19 , "Assistant_Manger":17 , "Employee":15 , "Worker" : 13, "Staff":10} 

with open("User_v1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id", "role", "grade"]
    writer.writerow(field)
    user_ids = []
    for i in range(30000):
        role = random.choice(roles)
        id = generate_id(user_ids)
        writer.writerow([id ,role , grades[role]])

start_date = datetime(2024, 10, 1, 0, 0, 0) 
with open("Message_v1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id", "value", "time"]
    writer.writerow(field)
    msg_ids = []
    for i in range(30000):
        id = generate_id(msg_ids)
        role = random.choice(roles)
        writer.writerow([id ,generate_message() , generate_random_datetime(start_date)])

with open("Group_v1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id", "name", "restrication"]
    writer.writerow(field)
    group_ids = []
    for i in range(30000):
        id = generate_id(group_ids)
        role = random.choice(roles)
        writer.writerow([id ,generate_name() , random.choice(["true" , "false"]) ])

with open("User_Message_v1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id", "source", "target" , "relation"]
    writer.writerow(field)
    receiver_msg =[]
    message_list = msg_ids.copy()
    user_list =  user_ids.copy()
    user_message_ids = []
    for i in range(10000):
        message_id = random.choice(message_list)
        message_list.remove(message_id) 
        receiver_msg.append(message_id)
        user_id =  random.choice(user_list)
        user_list.remove(user_id)
        writer.writerow([i+1 ,"USER_V1_"+ str(user_id) , "MESSAGE_V1_" + str(message_id) , "sender" ])
        writer.writerow([i+1 ,"MESSAGE_V1_" + str(message_id) ,"USER_V1_"+ str(user_id) , "send_by" ])
    print(len(receiver_msg))
    for i in range(8000):
        message_id = random.choice(receiver_msg)
        user_id = random.choice(user_ids)
        writer.writerow([i+1 ,"USER_V1_"+ str(user_id) ,"MESSAGE_V1_" + str(message_id) , "reciever" ])
        writer.writerow([i+1 ,"MESSAGE_V1_" +str(message_id) ,"USER_V1_"+ str(user_id) , "recied_by" ])
        receiver_msg.remove(message_id)

with open("User_Person_v1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id", "source", "target" , "relation"]
    writer.writerow(field)
    person_list = person_ids.copy()
    user_list = user_ids.copy()
    for i in range(2998):
        person_id =  random.choice(person_list)
        user_id = random.choice(user_list)
        person_list.remove(person_id)
        user_list.remove(user_id)
        writer.writerow([i+1 ,"USER_V1_"+ str(user_id) ,"PERSON_V1_"+ str(person_id) , "has_profile" ])
        writer.writerow([i+1 ,"PERSON_V1_"+str(person_id), "USER_V1_"+ str(user_id) , "has_account" ])
     

with open("User_Group_v1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id", "source", "target" , "relation"]
    writer.writerow(field)
    group_list = group_ids.copy()
    user_list = user_ids.copy()
    for i in range(20000):
        group_id = random.choice(group_list) 
        user_id =  random.choice(user_list)
        group_list.remove(group_id)
        user_list.remove(user_id)
        writer.writerow([i+1 ,"USER_V1_"+str(user_id) ,"GROUP_V1_"+ str(group_id) , "belong_to" ])
        writer.writerow([i+1 ,"GROUP_V1_"+ str(group_id) , "USER_V1_"+str(user_id) , "part_off" ])

# with open("Sample.csv" , 'w' , newline= "") as file:
#     writer = csv.writer(file)
#     field = [ "id", "name", "age", "country"]
#     writer.writerow(field)
#     for i in range(50):
#         writer.writerow([i+1 ,generate_name(), random.randint(18,60), random.choice(countries)])

with open("Sample1.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id", "role", "grade"]
    writer.writerow(field)
    for i in range(1000):
        role = random.choice(roles)
        writer.writerow([i+1 ,role , grades[role]])

# with open("Sample2.csv" , 'w' , newline= "") as file:
#     writer = csv.writer(file)
#     field = [ "id" ,"source", "target" , "relation"]
#     writer.writerow(field)
#     person_list = person_ids.copy()
#     user_list = user_ids.copy()
#     for i in range(997):
#         person_id =  random.choice(person_list)
#         user_id = random.choice(user_list)
#         person_list.remove(person_id)
#         user_list.remove(user_id)
#         writer.writerow([i+1 , "USER_"+str(user_id) , "PERSON_"+str(person_id) , "has_profile" ])
#         writer.writerow([i+1 , "PERSON_"+str(person_id) ,  "USER_"+ str(user_id) , "has_account" ])
     