from datetime import datetime

from app.api.schemas import (
    StudentSchema,
    FacultySchema,
    CourseSchema,
    EnrollmentSchema
)

from app.utils.file_utils import save_to_json, load_from_json

from app.services.database_service import (
    get_student_objects,
    get_faculty_objects,
    get_course_objects,
    get_enrollment_objects
)

from app.database.database import SessionLocal

from app.database.orm_models import (
    StudentORM,
    FacultyORM,
    CourseORM,
    EnrollmentORM
)


def export_all_data():
    save_to_json(get_student_objects(), "data/students.json")
    save_to_json(get_faculty_objects(), "data/faculty.json")
    save_to_json(get_course_objects(), "data/courses.json")
    save_to_json(get_enrollment_objects(), "data/enrollments.json")

    print("All data exported successfully")


def import_all_data():
    return {
        "students": load_from_json("data/students.json"),
        "faculty": load_from_json("data/faculty.json"),
        "courses": load_from_json("data/courses.json"),
        "enrollments": load_from_json("data/enrollments.json")
    }


def restore_all_data():
    data = import_all_data()
    db = SessionLocal()

    try:
        for record in data["students"]:
            validated = StudentSchema(**record)
            db.merge(StudentORM(**validated.model_dump()))

        for record in data["faculty"]:
            validated = FacultySchema(**record)
            db.merge(FacultyORM(**validated.model_dump()))

        db.flush()

        for record in data["courses"]:
            validated = CourseSchema(**record)
            db.merge(CourseORM(**validated.model_dump()))

        db.flush()

        for record in data["enrollments"]:
            enrollment_data = record.copy()

            enrollment_date = enrollment_data.pop("enrollment_date")
            datetime.fromisoformat(enrollment_date)

            validated = EnrollmentSchema(**enrollment_data)

            db.merge(
                EnrollmentORM(
                    **validated.model_dump(),
                    enrollment_date=enrollment_date
                )
            )

        db.commit()

        print("All data restored successfully")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()