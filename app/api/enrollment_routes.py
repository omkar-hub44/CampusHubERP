
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.enrollment import Enrollment
from app.services import enrollment_service
from app.api.schemas import EnrollmentSchema


router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("/", status_code=201)
def add_enrollment(enrollment: EnrollmentSchema):

    try:
        enrollment_obj = Enrollment(
            enrollment_id=enrollment.enrollment_id,
            student_id=enrollment.student_id,
            course_id=enrollment.course_id
        )

        return enrollment_service.add_enrollment(enrollment_obj)

    except ValueError as error:
        message = str(error)

        if message == "Student not found" or message == "Course not found":
            raise HTTPException(status_code=404, detail=message)

        raise HTTPException(status_code=409, detail=message)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Enrollment could not be created"
        )


@router.get("/")
def get_all_enrollments():
    return enrollment_service.get_all_enrollments()


@router.get("/{enrollment_id}")
def get_enrollment(enrollment_id: str):

    enrollment = enrollment_service.get_enrollment(enrollment_id)

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: str):

    deleted = enrollment_service.delete_enrollment(enrollment_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return {"message": "Enrollment deleted successfully"}
