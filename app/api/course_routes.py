
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.course import Course
from app.services import course_service, faculty_service
from app.api.schemas import CourseSchema


router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/", status_code=201)
def add_course(course: CourseSchema):

    if faculty_service.get_faculty(course.faculty_id) is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    try:
        course_obj = Course(**course.model_dump())
        return course_service.add_course(course_obj)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Course could not be created"
        )


@router.get("/")
def get_all_courses():
    return course_service.get_all_courses()


@router.get("/{course_id}")
def get_course(course_id: str):

    course = course_service.get_course(course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@router.put("/{course_id}")
def update_course(course_id: str, course: CourseSchema):

    if course_id != course.course_id:
        raise HTTPException(
            status_code=400,
            detail="Course ID cannot be changed"
        )

    if faculty_service.get_faculty(course.faculty_id) is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    try:
        updated_course = course_service.update_course(
            course_id,
            course_name=course.course_name,
            credits=course.credits,
            faculty_id=course.faculty_id
        )

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Course could not be updated"
        )

    if updated_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return updated_course


@router.delete("/{course_id}")
def delete_course(course_id: str):

    try:
        deleted = course_service.delete_course(course_id)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Course has existing enrollments"
        )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {"message": "Course deleted successfully"}
