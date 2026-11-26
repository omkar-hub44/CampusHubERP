import re


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def validate_student_id(student_id):
    return bool(re.fullmatch(r"ST[0-9]{3,}", student_id))


def validate_faculty_id(faculty_id):
    return bool(re.fullmatch(r"FC[0-9]{3,}", faculty_id))


def validate_course_id(course_id):
    return bool(re.fullmatch(r"CS[0-9]{3,}", course_id))


def validate_enrollment_id(enrollment_id):
    return bool(re.fullmatch(r"EN[0-9]{3,}", enrollment_id))