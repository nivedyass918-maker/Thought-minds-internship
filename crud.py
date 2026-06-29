from sqlalchemy.orm import Session
import models
import schemas

# CREATE
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        age=student.age,
        course=student.course
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# GET ALL
def get_students(db: Session):
    return db.query(models.Student).all()

# GET BY ID
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

# UPDATE
def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not db_student:
        return {"error": "Student not found"}

    db_student.name = student.name
    db_student.age = student.age
    db_student.course = student.course

    db.commit()
    db.refresh(db_student)
    return db_student

# DELETE
def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not db_student:
        return {"error": "Student not found"}

    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}
