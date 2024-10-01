from fastapi import FastAPI
from pymongo import MongoClient
import json
from pymongo.collection import Collection 
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
import motor
from models import Student , StudentResponce
import uvicorn
from bson import ObjectId
import logging


# mongodb://localhost:27017/
MONGO_DETAIL = "mongodb://localhost:27017/"
client =  MongoClient(MONGO_DETAIL)
database = client.Test
student_collection = database.get_collection("Students")

app  = FastAPI( debug=True)

@app.get("/")
def start():
    return("Hello World")


@app.post("/post-student")
def post_student(student :Student ):
    student = student.dict()
    result  =  student_collection.insert_one(student)
    student['_id'] = str(result.inserted_id)
    return student
    


@app.post()

@app.get("/get-student/{id}")
def  get_student(id : str):

    print("asd")
   
    student =  student_collection.find_one({"_id" : ObjectId(id) })
    student["_id"] = str(student["_id"])  # Convert ObjectId to string
    return student


@app.get("/get-all",response_model=list[StudentResponce])
def get_all() -> list[StudentResponce]:
    students = student_collection.find()
    return_list = []
    for student in students :
        # student["id"] = str(student["_id"])
        # # Remove the _id field if it's not needed
        # del student["_id"]
        responce_student = StudentResponce(**student)
        responce_student.id = str(student["_id"])
        return_list.append(responce_student)
        # print(student.name)

    students = [Student(**student) for student in students]
    print(return_list)
    return return_list


@app.delete("/delete/{id}")
def delete(id : str):
    result = student_collection.find_one_and_delete({"_id" : ObjectId(id) })
    # result.id = str(result["_id"])
    responce = StudentResponce(**result)
    responce.id = str(result["_id"])
    logging.info("this is first logging" , result)
    print(responce)


    return responce
    



if __name__ == "__main__":
    print("Running FastAPI server...")
    print("Swagger UI available at: http://127.0.0.1:8000/docs")
    print("ReDoc available at: http://127.0.0.1:8000/redoc")

    uvicorn.run("FastApi:app", host="127.0.0.1", port=8000, reload=True)

    # app.run(host="127.0.0.1", port=8000, reload=True)  
    