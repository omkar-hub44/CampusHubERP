from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.database import get_db
from app.services.database_service import DatabaseService
from app.api.schemas import StudentSchema


router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", status_code=201)
def add_student(student: StudentSchema, db: Session = Depends(get_db)):
    service = DatabaseService(db)

    try:
        return service.students.create(student.model_dump())
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Student ID or email already exists"
        )


@router.get("/")
def get_all_students(db: Session = Depends(get_db)):
    service = DatabaseService(db)
    return service.students.get_all()


@router.get("/{student_id}")
def get_student(student_id: str, db: Session = Depends(get_db)):
    service = DatabaseService(db)
    student = service.students.get_by_id(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.put("/{student_id}")
def update_student(
    student_id: str,
    student: StudentSchema,
    db: Session = Depends(get_db)
):
    service = DatabaseService(db)

    if student_id != student.student_id:
        raise HTTPException(
            status_code=400,
            detail="Student ID cannot be changed"
        )

    try:
        updated_student = service.students.update(
            student_id,
            student.model_dump(exclude={"student_id"})
        )
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")

    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return updated_student


@router.delete("/{student_id}")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    service = DatabaseService(db)

    try:
        deleted = service.students.delete(student_id)
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Student has existing enrollments"
        )

    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}