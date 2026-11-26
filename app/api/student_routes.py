
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.student import Student
from app.services import student_service
from app.api.schemas import StudentSchema


router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", status_code=201)
def add_student(student: StudentSchema):

    try:
        student_obj = Student(**student.model_dump())
        return student_service.add_student(student_obj)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Student ID or email already exists"
        )

    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))


@router.get("/")
def get_all_students():
    return student_service.get_all_students()


@router.get("/{student_id}")
def get_student(student_id: str):

    student = student_service.get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put("/{student_id}")
def update_student(student_id: str, student: StudentSchema):

    if student_id != student.student_id:
        raise HTTPException(
            status_code=400,
            detail="Student ID cannot be changed"
        )

    try:
        updated_student = student_service.update_student(
            student_id,
            name=student.name,
            age=student.age,
            email=student.email,
            department=student.department
        )

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


@router.delete("/{student_id}")
def delete_student(student_id: str):

    try:
        deleted = student_service.delete_student(student_id)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Student has existing enrollments"
        )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }
