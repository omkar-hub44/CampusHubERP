
from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.database.orm_models import EnrollmentORM
from app.database.repository import Repository
from app.services.student_service import get_student
from app.services.course_service import get_course
from app.utils.decorators import log_execution, measure_time


@log_execution
@measure_time
def add_enrollment(enrollment):

    if get_student(enrollment.student_id) is None:
        raise ValueError("Student not found")

    if get_course(enrollment.course_id) is None:
        raise ValueError("Course not found")

    db = SessionLocal()

    try:
        repository = Repository(db, EnrollmentORM)

        if repository.get_by_id(enrollment.enrollment_id):
            raise ValueError("Enrollment ID already exists")

        existing_enrollments = repository.get_all()

        for existing in existing_enrollments:
            if (existing.student_id == enrollment.student_id
                    and existing.course_id == enrollment.course_id):
                raise ValueError(
                    "Student already enrolled in this course"
                )

        return repository.create(enrollment.to_dict())

    except IntegrityError as error:
        db.rollback()
        raise ValueError(
            "Duplicate or invalid enrollment"
        ) from error

    finally:
        db.close()


def get_all_enrollments():
    db = SessionLocal()

    try:
        repository = Repository(db, EnrollmentORM)
        return repository.get_all()

    finally:
        db.close()


def get_enrollment(enrollment_id):
    db = SessionLocal()

    try:
        repository = Repository(db, EnrollmentORM)
        return repository.get_by_id(enrollment_id)

    finally:
        db.close()


def delete_enrollment(enrollment_id):
    db = SessionLocal()

    try:
        repository = Repository(db, EnrollmentORM)
        return repository.delete(enrollment_id)

    finally:
        db.close()
