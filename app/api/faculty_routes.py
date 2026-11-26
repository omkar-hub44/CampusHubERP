
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.faculty import Faculty
from app.services import faculty_service
from app.api.schemas import FacultySchema


router = APIRouter(prefix="/faculty", tags=["Faculty"])


@router.post("/", status_code=201)
def add_faculty(faculty: FacultySchema):

    try:
        faculty_obj = Faculty(**faculty.model_dump())
        return faculty_service.add_faculty(faculty_obj)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Faculty ID or email already exists"
        )

    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))


@router.get("/")
def get_all_faculty():
    return faculty_service.get_all_faculty()


@router.get("/{faculty_id}")
def get_faculty(faculty_id: str):

    faculty = faculty_service.get_faculty(faculty_id)

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return faculty


@router.put("/{faculty_id}")
def update_faculty(faculty_id: str, faculty: FacultySchema):

    if faculty_id != faculty.faculty_id:
        raise HTTPException(
            status_code=400,
            detail="Faculty ID cannot be changed"
        )

    try:
        updated_faculty = faculty_service.update_faculty(
            faculty_id,
            name=faculty.name,
            age=faculty.age,
            email=faculty.email,
            department=faculty.department
        )

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    if updated_faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return updated_faculty


@router.delete("/{faculty_id}")
def delete_faculty(faculty_id: str):

    try:
        deleted = faculty_service.delete_faculty(faculty_id)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Faculty has existing courses"
        )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return {"message": "Faculty deleted successfully"}
