from fastapi import FastAPI, Query
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "postgresql://postgres:123456@db:5432/students_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



class Student(Base):
    __tablename__ = "studentsinfo"  # Tên bảng trong cơ sở dữ liệu

    id = Column(Integer, primary_key=True, autoincrement=True)  # Thêm ID làm khóa chính
    last_name = Column(String, nullable=False)  # Thêm trường фамилия (last_name)
    first_name = Column(String, nullable=False)  # Thêm trường имя (first_name)
    middle_name = Column(String, nullable=False)  # Thêm trường отчество (middle_name)
    course = Column(Integer, nullable=False)  # Thêm trường курс (course), có thể là Integer
    group_name = Column(String, nullable=False)  # Thêm trường группа (group_name)
    faculty = Column(String, nullable=False)  # Thêm trường факультет (faculty)


class StudentCreate(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    course: int
    group_name: str
    faculty: str

class StudentOut(BaseModel):
    id: int
    last_name: str
    first_name: str
    middle_name: str
    course: int
    group_name: str
    faculty: str

    class Config:
        orm_mode = True

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/students/", response_model=list[StudentOut])
def list_students(page: int, page_size: int):
    db = SessionLocal()
    students = db.query(Student).offset((page - 1) * page_size).limit(page_size).all()
    db.close()
    return students
@app.post("/students/", response_model=StudentOut)
def create_student(student: StudentCreate):
    db = SessionLocal()
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)  # Lấy bản ghi mới được thêm từ database
    db.close()
    return new_student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        db.close()
        return {"error": "Student not found"}
    db.delete(student)
    db.commit()
    db.close()
    return {"message": "Student deleted successfully"}

