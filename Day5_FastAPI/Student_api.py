from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student
    return {"message": "Student not found"}

@app.post("/students")
def add_student(student: Student):
    students.append(student.dict())
    return {"message": "Student added successfully"}