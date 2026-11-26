
from app.database.database import SessionLocal
from app.database.orm_models import FacultyORM
from app.database.repository import Repository
from app.utils.decorators import log_execution, measure_time


@log_execution
@measure_time
def add_faculty(faculty):
    db = SessionLocal()

    try:
        repository = Repository(db, FacultyORM)
        return repository.create(faculty.to_dict())

    finally:
        db.close()


def get_all_faculty():
    db = SessionLocal()

    try:
        repository = Repository(db, FacultyORM)
        return repository.get_all()

    finally:
        db.close()


def get_faculty(faculty_id):
    db = SessionLocal()

    try:
        repository = Repository(db, FacultyORM)
        return repository.get_by_id(faculty_id)

    finally:
        db.close()


def update_faculty(faculty_id, **kwargs):
    db = SessionLocal()

    try:
        repository = Repository(db, FacultyORM)

        allowed_fields = ("name", "age", "email", "department")

        valid_data = {
            key: value
            for key, value in kwargs.items()
            if key in allowed_fields
        }

        return repository.update(faculty_id, valid_data)

    finally:
        db.close()


def delete_faculty(faculty_id):
    db = SessionLocal()

    try:
        repository = Repository(db, FacultyORM)
        return repository.delete(faculty_id)

    finally:
        db.close()
