from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Student API is running successfully"}

@app.post("/students")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id)
@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student)
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id)