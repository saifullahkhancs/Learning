from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, InvalidOperation
import json
from pymongo.collection import Collection 
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
import motor
from models import Student , StudentResponce
import uvicorn
from bson import ObjectId
from bson.errors import InvalidId
import logging

logger = logging.getLogger(__name__)


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
    try:
        obj_id = ObjectId(id)
    except (InvalidId, TypeError):
        raise HTTPException(status_code=400, detail=f"Invalid student ID format: {id}")

    student = student_collection.find_one({"_id": obj_id})
    if student is None:
        raise HTTPException(status_code=404, detail=f"Student with id '{id}' not found")
    student["_id"] = str(student["_id"])
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
    try:
        obj_id = ObjectId(id)
    except (InvalidId, TypeError):
        raise HTTPException(status_code=400, detail=f"Invalid student ID format: {id}")

    result = student_collection.find_one_and_delete({"_id" : obj_id })
    if result is None:
        raise HTTPException(status_code=404, detail=f"Student with id '{id}' not found")
    responce = StudentResponce(**result)
    responce.id = str(result["_id"])
    logger.info(f"Deleted student: {responce.id}")

    return responce
    



if __name__ == "__main__":
    print("Running FastAPI server...")
    print("Swagger UI available at: http://127.0.0.1:8000/docs")
    print("ReDoc available at: http://127.0.0.1:8000/redoc")

    uvicorn.run("FastApi:app", host="127.0.0.1", port=8000, reload=True)

    # app.run(host="127.0.0.1", port=8000, reload=True)  
    