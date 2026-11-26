from app.database.database import Base, engine, SessionLocal
from app.database.orm_models import (
    StudentORM,
    FacultyORM,
    CourseORM,
    EnrollmentORM
)


def seed_data():
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:

        try:
            db.merge(StudentORM(
                student_id="ST001",
                name="Rahul",
                age=20,
                email="rahul@gmail.com",
                department="CS"
            ))

            db.merge(StudentORM(
                student_id="ST002",
                name="Priya",
                age=21,
                email="priya@gmail.com",
                department="IT"
            ))

            db.merge(FacultyORM(
                faculty_id="FC001",
                name="Amit",
                age=35,
                email="amit@gmail.com",
                department="CS"
            ))

            db.flush()

            db.merge(CourseORM(
                course_id="CS001",
                course_name="Python Programming",
                credits=4,
                faculty_id="FC001"
            ))

            db.flush()

            db.merge(EnrollmentORM(
                enrollment_id="EN001",
                student_id="ST001",
                course_id="CS001",
                enrollment_date="2026-11-26"
            ))

            db.commit()

            print("Sample data inserted successfully")

        except Exception:
            db.rollback()
            raise


if __name__ == "__main__":
    seed_data()