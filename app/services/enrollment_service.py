from app.models.enrollment import Enrollment
from app.services.student_service import get_student
from app.services.course_service import get_course

enrollments = []


def add_enrollment(enrollment):
    if get_student(enrollment.student_id) is None:
        raise ValueError("Student not found")

    if get_course(enrollment.course_id) is None:
        raise ValueError("Course not found")

    for existing in enrollments:
        if existing.enrollment_id == enrollment.enrollment_id:
            raise ValueError("Enrollment ID already exists")

        if (existing.student_id == enrollment.student_id
                and existing.course_id == enrollment.course_id):
            raise ValueError("Student already enrolled in this course")

    enrollments.append(enrollment)
    return enrollment


def get_all_enrollments():
    return enrollments


def get_enrollment(enrollment_id):
    for enrollment in enrollments:
        if enrollment.enrollment_id == enrollment_id:
            return enrollment
    return None


def delete_enrollment(enrollment_id):
    enrollment = get_enrollment(enrollment_id)

    if enrollment:
        enrollments.remove(enrollment)
        return True

    return False