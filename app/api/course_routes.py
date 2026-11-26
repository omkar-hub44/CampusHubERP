from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.database import get_db
from app.services.database_service import DatabaseService
from app.api.schemas import CourseSchema


router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/", status_code=201)
def add_course(course: CourseSchema, db: Session = Depends(get_db)):
    service = DatabaseService(db)

    if service.faculty.get_by_id(course.faculty_id) is None:
        raise HTTPException(status_code=404, detail="Faculty not found")

    try:
        return service.courses.create(course.model_dump())
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Course could not be created")


@router.get("/")
def get_all_courses(db: Session = Depends(get_db)):
    service = DatabaseService(db)
    return service.courses.get_all()


@router.get("/{course_id}")
def get_course(course_id: str, db: Session = Depends(get_db)):
    service = DatabaseService(db)
    course = service.courses.get_by_id(course_id)

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return course


@router.put("/{course_id}")
def update_course(
    course_id: str,
    course: CourseSchema,
    db: Session = Depends(get_db)
):
    service = DatabaseService(db)

    if course_id != course.course_id:
        raise HTTPException(
            status_code=400,
            detail="Course ID cannot be changed"
        )

    if service.faculty.get_by_id(course.faculty_id) is None:
        raise HTTPException(status_code=404, detail="Faculty not found")

    try:
        updated_course = service.courses.update(
            course_id,
            course.model_dump(exclude={"course_id"})
        )
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Course could not be updated")

    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return updated_course


@router.delete("/{course_id}")
def delete_course(course_id: str, db: Session = Depends(get_db)):
    service = DatabaseService(db)

    try:
        deleted = service.courses.delete(course_id)
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Course has existing enrollments"
        )

    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")

    return {"message": "Course deleted successfully"}