from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.database import get_db
from app.services.database_service import DatabaseService
from app.api.schemas import FacultySchema


router = APIRouter(prefix="/faculty", tags=["Faculty"])


@router.post("/", status_code=201)
def add_faculty(faculty: FacultySchema, db: Session = Depends(get_db)):
    service = DatabaseService(db)

    try:
        return service.faculty.create(faculty.model_dump())
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Faculty ID or email already exists"
        )


@router.get("/")
def get_all_faculty(db: Session = Depends(get_db)):
    service = DatabaseService(db)
    return service.faculty.get_all()


@router.get("/{faculty_id}")
def get_faculty(faculty_id: str, db: Session = Depends(get_db)):
    service = DatabaseService(db)
    faculty = service.faculty.get_by_id(faculty_id)

    if faculty is None:
        raise HTTPException(status_code=404, detail="Faculty not found")

    return faculty


@router.put("/{faculty_id}")
def update_faculty(
    faculty_id: str,
    faculty: FacultySchema,
    db: Session = Depends(get_db)
):
    service = DatabaseService(db)

    if faculty_id != faculty.faculty_id:
        raise HTTPException(
            status_code=400,
            detail="Faculty ID cannot be changed"
        )

    try:
        updated_faculty = service.faculty.update(
            faculty_id,
            faculty.model_dump(exclude={"faculty_id"})
        )
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")

    if updated_faculty is None:
        raise HTTPException(status_code=404, detail="Faculty not found")

    return updated_faculty


@router.delete("/{faculty_id}")
def delete_faculty(faculty_id: str, db: Session = Depends(get_db)):
    service = DatabaseService(db)

    try:
        deleted = service.faculty.delete(faculty_id)
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Faculty has existing courses"
        )

    if not deleted:
        raise HTTPException(status_code=404, detail="Faculty not found")

    return {"message": "Faculty deleted successfully"}