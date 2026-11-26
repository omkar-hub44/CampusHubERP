from app.utils.file_utils import save_to_json, load_from_json

from app.services.database_service import (
    get_student_objects,
    get_faculty_objects,
    get_course_objects,
    get_enrollment_objects
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