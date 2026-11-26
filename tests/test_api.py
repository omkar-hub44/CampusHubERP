
import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database.database import Base

from app.services import (
    student_service,
    faculty_service,
    course_service,
    enrollment_service
)


@pytest.fixture
def client(monkeypatch):

    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )

    @event.listens_for(engine, "connect")
    def enable_foreign_keys(connection, record):
        connection.execute("PRAGMA foreign_keys=ON")

    Base.metadata.create_all(bind=engine)

    TestingSession = sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    # Connect all service modules to the temporary test database
    monkeypatch.setattr(
        student_service, "SessionLocal", TestingSession
    )

    monkeypatch.setattr(
        faculty_service, "SessionLocal", TestingSession
    )

    monkeypatch.setattr(
        course_service, "SessionLocal", TestingSession
    )

    monkeypatch.setattr(
        enrollment_service, "SessionLocal", TestingSession
    )

    try:
        with TestClient(app) as test_client:
            yield test_client

    finally:
        engine.dispose()


student_data = {
    "student_id": "ST001",
    "name": "Rahul",
    "age": 20,
    "email": "rahul@gmail.com",
    "department": "CS"
}

faculty_data = {
    "faculty_id": "FC001",
    "name": "Amit",
    "age": 35,
    "email": "amit@gmail.com",
    "department": "CS"
}

course_data = {
    "course_id": "CS001",
    "course_name": "Python Programming",
    "credits": 4,
    "faculty_id": "FC001"
}

enrollment_data = {
    "enrollment_id": "EN001",
    "student_id": "ST001",
    "course_id": "CS001"
}


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_create_student(client):
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201


def test_get_students(client):
    client.post("/students/", json=student_data)
    response = client.get("/students/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_student(client):
    client.post("/students/", json=student_data)
    response = client.get("/students/ST001")

    assert response.status_code == 200
    assert response.json()["name"] == "Rahul"


def test_update_student(client):
    client.post("/students/", json=student_data)

    updated_data = {**student_data, "age": 21}
    response = client.put("/students/ST001", json=updated_data)

    assert response.status_code == 200
    assert response.json()["age"] == 21


def test_delete_student(client):
    client.post("/students/", json=student_data)
    response = client.delete("/students/ST001")

    assert response.status_code == 200
    assert client.get("/students/ST001").status_code == 404


def test_student_not_found(client):
    response = client.get("/students/ST999")
    assert response.status_code == 404


def test_duplicate_student(client):
    client.post("/students/", json=student_data)
    response = client.post("/students/", json=student_data)

    assert response.status_code == 409


def test_invalid_student_age(client):
    invalid_data = {**student_data, "age": 10}
    response = client.post("/students/", json=invalid_data)

    assert response.status_code == 422


def test_invalid_student_email(client):
    invalid_data = {**student_data, "email": "invalidemail"}
    response = client.post("/students/", json=invalid_data)

    assert response.status_code == 422


def test_create_faculty(client):
    response = client.post("/faculty/", json=faculty_data)
    assert response.status_code == 201


def test_create_course(client):
    client.post("/faculty/", json=faculty_data)
    response = client.post("/courses/", json=course_data)

    assert response.status_code == 201


def test_course_invalid_faculty(client):
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 404


def test_create_enrollment(client):
    client.post("/students/", json=student_data)
    client.post("/faculty/", json=faculty_data)
    client.post("/courses/", json=course_data)

    response = client.post(
        "/enrollments/", json=enrollment_data
    )

    assert response.status_code == 201


def test_duplicate_enrollment(client):
    client.post("/students/", json=student_data)
    client.post("/faculty/", json=faculty_data)
    client.post("/courses/", json=course_data)
    client.post("/enrollments/", json=enrollment_data)

    duplicate_data = {
        **enrollment_data,
        "enrollment_id": "EN002"
    }

    response = client.post(
        "/enrollments/", json=duplicate_data
    )

    assert response.status_code == 409


def test_enrollment_invalid_student(client):
    response = client.post(
        "/enrollments/", json=enrollment_data
    )

    assert response.status_code == 404


def test_blank_student_name(client):
    invalid_data = {**student_data, "name": "   "}

    response = client.post("/students/", json=invalid_data)

    assert response.status_code == 422


def test_unexpected_student_field(client):
    invalid_data = {**student_data, "unknown_field": "test"}

    response = client.post("/students/", json=invalid_data)

    assert response.status_code == 422
