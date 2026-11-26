
from app.database.database import SessionLocal
from app.database.orm_models import CourseORM
from app.database.repository import Repository
from app.utils.decorators import log_execution, measure_time


@log_execution
@measure_time
def add_course(course):
    db = SessionLocal()

    try:
        repository = Repository(db, CourseORM)
        return repository.create(course.to_dict())

    finally:
        db.close()


def get_all_courses():
    db = SessionLocal()

    try:
        repository = Repository(db, CourseORM)
        return repository.get_all()

    finally:
        db.close()


def get_course(course_id):
    db = SessionLocal()

    try:
        repository = Repository(db, CourseORM)
        return repository.get_by_id(course_id)

    finally:
        db.close()


def update_course(course_id, **kwargs):
    db = SessionLocal()

    try:
        repository = Repository(db, CourseORM)

        allowed_fields = ("course_name", "credits", "faculty_id")

        valid_data = {
            key: value
            for key, value in kwargs.items()
            if key in allowed_fields
        }

        return repository.update(course_id, valid_data)

    finally:
        db.close()


def delete_course(course_id):
    db = SessionLocal()

    try:
        repository = Repository(db, CourseORM)
        return repository.delete(course_id)

    finally:
        db.close()
