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

        tasks = [
            executor.submit(generate_student_report, students),
            executor.submit(generate_faculty_report, faculty_members),
            executor.submit(generate_course_report, courses),
            executor.submit(generate_enrollment_report, enrollments)
        ]

        for task in tasks:
            task.result()

    print("All reports generated successfully")