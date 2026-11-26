from app.utils.generators import (
    student_generator,
    faculty_generator,
    course_generator
)
from app.utils.context_managers import ReportWriter


def generate_student_report(students):
    with ReportWriter("reports/student_report.txt") as file:
        file.write("STUDENT REPORT\n")
        file.write("=" * 40 + "\n")

        for student in student_generator(students):
            file.write(str(student.to_dict()) + "\n")

    print("Student report generated successfully")


def generate_faculty_report(faculty_members):
    with ReportWriter("reports/faculty_report.txt") as file:
        file.write("FACULTY REPORT\n")
        file.write("=" * 40 + "\n")

        for faculty in faculty_generator(faculty_members):
            file.write(str(faculty.to_dict()) + "\n")

    print("Faculty report generated successfully")


def generate_course_report(courses):
    with ReportWriter("reports/course_report.txt") as file:
        file.write("COURSE REPORT\n")
        file.write("=" * 40 + "\n")

        for course in course_generator(courses):
            file.write(str(course.to_dict()) + "\n")

    print("Course report generated successfully")

def generate_all_database_reports():

    from app.services.database_service import (
        get_student_objects,
        get_faculty_objects,
        get_course_objects,
        get_enrollment_objects
    )

    generate_student_report(get_student_objects())
    generate_faculty_report(get_faculty_objects())
    generate_course_report(get_course_objects())
    generate_enrollment_report(get_enrollment_objects())

    print("All database reports generated successfully")

def generate_enrollment_report(enrollments):

    with ReportWriter("reports/enrollment_report.txt") as file:

        file.write("ENROLLMENT REPORT\n")
        file.write("=" * 40 + "\n")

        for enrollment in enrollments:
            file.write(str(enrollment.to_dict()) + "\n")

    print("Enrollment report generated successfully")