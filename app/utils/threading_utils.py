
from concurrent.futures import ThreadPoolExecutor

from app.services.report_service import (
    generate_student_report,
    generate_faculty_report,
    generate_course_report,
    generate_enrollment_report
)


def generate_reports_concurrently(
    students, faculty_members, courses, enrollments
):

    with ThreadPoolExecutor(max_workers=4) as executor:

        print("Generating Student Report...")
        student_task = executor.submit(
            generate_student_report, students
        )

        print("Generating Faculty Report...")
        faculty_task = executor.submit(
            generate_faculty_report, faculty_members
        )

        print("Generating Course Report...")
        course_task = executor.submit(
            generate_course_report, courses
        )

        print("Generating Enrollment Report...")
        enrollment_task = executor.submit(
            generate_enrollment_report, enrollments
        )

        student_task.result()
        faculty_task.result()
        course_task.result()
        enrollment_task.result()

    print("Done.")
    print("All reports generated successfully")
