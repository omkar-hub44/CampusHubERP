from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.database import Base
from app.database.orm_models import (
    StudentORM,
    FacultyORM,
    CourseORM,
    EnrollmentORM
)

from app.services import data_service


def test_restore_all_data(monkeypatch):
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    TestSession = sessionmaker(bind=engine)

    monkeypatch.setattr(
        data_service,
        "SessionLocal",
        TestSession
    )

    try:
        data_service.restore_all_data()

        with TestSession() as db:
            assert db.query(StudentORM).count() == 2
            assert db.query(FacultyORM).count() == 1
            assert db.query(CourseORM).count() == 1
            assert db.query(EnrollmentORM).count() == 1

    finally:
        engine.dispose()