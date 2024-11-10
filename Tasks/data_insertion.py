import csv 
import random
import string
from datetime import datetime, timedelta


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

with open("Person.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" "name", "age", "country"]

    for i in range(1000):
        writer.writerow([i+1 ,generate_name(), random.randint(14,60), random.choice(countries)])


roles = ["Manager" , "Assistant_Manger" , "Employee", "Worker", "Staff"]
grades = {"Manager": 19 , "Assistant_Manger":17 , "Employee":15 , "Worker" : 13, "Staff":10} 

with open("User.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" "role", "grade"]

    for i in range(1000):
        role = random.choice(roles)
        writer.writerow([i+1 ,role , grades[role]])

start_date = datetime(2024, 10, 1, 0, 0, 0) 
with open("Msg.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" "value", "time"]
    for i in range(1000):
        role = random.choice(roles)
        writer.writerow([i+1 ,generate_message() , generate_random_datetime(start_date)])

with open("Group.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" "name", "restrication"]
    for i in range(1000):
        role = random.choice(roles)
        writer.writerow([i+1 ,generate_name() , random.choice(["true" , "false"]) ])

def generate_id(IdList):
    id  = random.randint(1,1000)
    if id in IdList:
        generate_id(IdList)
    else:
        IdList.append(id)
        return id


with open("User_Message.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" "user_id", "message_id" , "relation"]
    message_list = []
    user_list = []
    for i in range(300):
        message_id = generate_id(message_list)  
        user_id =  generate_id(user_list)
        writer.writerow([i+1 ,user_id , message_id , "sender" ])
        writer.writerow([i+1 ,user_id , message_id , "send_by" ])

    for i in range(300):
        message_id = random.choice(message_list)
        user_id = random.randint(1,1000)
        writer.writerow([i+1 ,user_id , message_id , "reciever" ])
        writer.writerow([i+1 ,user_id , message_id , "recied_by" ])
        message_list.remove(message_id)


with open("User_Person.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" "user_id", "person_id" , "relation"]
    person_list = []
    user_list = []
    for i in range(999):
        person_id = generate_id(person_list)  
        user_id =  generate_id(user_list)
        writer.writerow([i+1 ,user_id , person_id , "has_profile" ])
        writer.writerow([i+1 ,user_id,  person_id , "has_account" ])
     

with open("User_Group.csv" , 'w' , newline= "") as file:
    writer = csv.writer(file)
    field = [ "id" "user_id", "group_id" , "relation"]
    group_list = []
    user_list = []
    for i in range(500):
        group_id = random.randint(1,1000)  
        user_id =  random.randint(1,1000)
        writer.writerow([i+1 ,user_id , group_id , "belong_to" ])
        writer.writerow([i+1 ,user_id , group_id , "part_off" ])