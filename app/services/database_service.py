from app.core.factory import ModelFactory
from app.core.singleton import DatabaseManager
from app.database.repository import Repository
from app.database.orm_models import (
    StudentORM,
    FacultyORM,
    CourseORM,
    EnrollmentORM
)


class DatabaseService:

    def __init__(self, db):
        self.students = Repository(db, StudentORM)
        self.faculty = Repository(db, FacultyORM)
        self.courses = Repository(db, CourseORM)
        self.enrollments = Repository(db, EnrollmentORM)


def get_database_summary():

    with DatabaseManager().get_session() as db:
        service = DatabaseService(db)

        return {
            "total_students": len(service.students.get_all()),
            "total_faculty": len(service.faculty.get_all()),
            "total_courses": len(service.courses.get_all()),
            "total_enrollments": len(service.enrollments.get_all())
        }

def get_student_objects():

    with DatabaseManager().get_session() as db:
        service = DatabaseService(db)

        return [
            ModelFactory.create_model(
                "student",
                student_id=record.student_id,
                name=record.name,
                age=record.age,
                email=record.email,
                department=record.department
            )
            for record in service.students.get_all()
        ]

def get_faculty_objects():

    with DatabaseManager().get_session() as db:
        service = DatabaseService(db)

        return [
            ModelFactory.create_model(
                "faculty",
                faculty_id=record.faculty_id,
                name=record.name,
                age=record.age,
                email=record.email,
                department=record.department
            )
            for record in service.faculty.get_all()
        ]


def get_course_objects():

    with DatabaseManager().get_session() as db:
        service = DatabaseService(db)

        return [
            ModelFactory.create_model(
                "course",
                course_id=record.course_id,
                course_name=record.course_name,
                credits=record.credits,
                faculty_id=record.faculty_id
            )
            for record in service.courses.get_all()
        ]


def get_enrollment_objects():

    with DatabaseManager().get_session() as db:
        service = DatabaseService(db)

        enrollments = []

        for record in service.enrollments.get_all():
            enrollment = ModelFactory.create_model(
                "enrollment",
                enrollment_id=record.enrollment_id,
                student_id=record.student_id,
                course_id=record.course_id
            )

            enrollment.enrollment_date = record.enrollment_date
            enrollments.append(enrollment)

        return enrollments    