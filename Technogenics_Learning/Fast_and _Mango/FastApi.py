from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.collection import Collection 
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
import motor
from models import Student
import uvicorn
from bson import ObjectId


# mongodb://localhost:27017/
MONGO_DETAIL = "mongodb://localhost:27017/"
client =  motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAIL)
database = client.Test
student_collection = database.get_collection("Students")

app  = FastAPI( debug=True)

@app.get("/")
def start():
    return("Hello World")


@app.post("/post_student")
async def post_student(student :Student ):
    student = student.dict()
    result  = await student_collection.insert_one(student)
    student['_id'] = str(result.inserted_id)
    return student
    


@app.get("/get_student/{id}")
async def  get_student(id : str):

    print("asd")
   
    student =  await student_collection.find_one({"_id" : ObjectId(id) })
    student["_id"] = str(student["_id"])  # Convert ObjectId to string
    return student


if __name__ == "__main__":
    print("Running FastAPI server...")
    print("Swagger UI available at: http://127.0.0.1:8000/docs")
    print("ReDoc available at: http://127.0.0.1:8000/redoc")

    uvicorn.run("FastApi:app", host="127.0.0.1", port=8000, reload=True)

    # app.run(host="127.0.0.1", port=8000, reload=True)  
    