
from app.models.student import Student
from app.database.database import SessionLocal
from app.database.orm_models import StudentORM
from app.database.repository import Repository
from app.utils.decorators import log_execution, measure_time


@log_execution
@measure_time
def add_student(student):
    db = SessionLocal()

    try:
        repository = Repository(db, StudentORM)
        return repository.create(student.to_dict())

    finally:
        db.close()


def get_all_students():
    db = SessionLocal()

    try:
        repository = Repository(db, StudentORM)
        return repository.get_all()

    finally:
        db.close()


def get_student(student_id):
    db = SessionLocal()

    try:
        repository = Repository(db, StudentORM)
        return repository.get_by_id(student_id)

    finally:
        db.close()


def update_student(student_id, **kwargs):
    db = SessionLocal()

    try:
        repository = Repository(db, StudentORM)

        allowed_fields = ("name", "age", "email", "department")

        valid_data = {
            key: value
            for key, value in kwargs.items()
            if key in allowed_fields
        }

        return repository.update(student_id, valid_data)

    finally:
        db.close()


def delete_student(student_id):
    db = SessionLocal()

    try:
        repository = Repository(db, StudentORM)
        return repository.delete(student_id)

    finally:
        db.close()
