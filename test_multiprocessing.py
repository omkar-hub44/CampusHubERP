from app.utils.multiprocessing_utils import calculate_totals

from app.services.database_service import (
    get_student_objects,
    get_faculty_objects,
    get_course_objects,
    get_enrollment_objects
)


if __name__ == "__main__":

    students = get_student_objects()
    faculty = get_faculty_objects()
    courses = get_course_objects()
    enrollments = get_enrollment_objects()

    totals = calculate_totals(
        students,
        faculty,
        courses,
        enrollments
    )

    print(totals)