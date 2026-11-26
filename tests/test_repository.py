import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.database import Base
from app.database.orm_models import StudentORM
from app.database.repository import Repository


@pytest.fixture
def repository():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    db = Session()

    try:
        yield Repository(db, StudentORM)
    finally:
        db.close()
        engine.dispose()


@pytest.fixture
def student_data():
    return {
        "student_id": "ST001",
        "name": "Rahul",
        "age": 20,
        "email": "rahul@gmail.com",
        "department": "CS"
    }


def test_create_student(repository, student_data):
    student = repository.create(student_data)

    assert student.student_id == "ST001"
    assert student.name == "Rahul"


def test_get_all_students(repository, student_data):
    repository.create(student_data)

    students = repository.get_all()

    assert len(students) == 1


def test_get_student_by_id(repository, student_data):
    repository.create(student_data)

    student = repository.get_by_id("ST001")

    assert student.name == "Rahul"


def test_update_student(repository, student_data):
    repository.create(student_data)

    student = repository.update("ST001", {"age": 21})

    assert student.age == 21


def test_delete_student(repository, student_data):
    repository.create(student_data)

    assert repository.delete("ST001") is True
    assert repository.get_by_id("ST001") is None


def test_student_not_found(repository):
    assert repository.get_by_id("ST999") is None


def test_delete_nonexistent_student(repository):
    assert repository.delete("ST999") is False