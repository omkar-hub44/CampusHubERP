from app.models.student import Student
from app.utils.decorators import log_execution, measure_time

students = []


@log_execution
@measure_time
def add_student(student):
    students.append(student)
    return student


def get_all_students():
    return students


def get_student(student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None


def update_student(student_id, **kwargs):
    student = get_student(student_id)

    if student:
        for key, value in kwargs.items():
            if key in ("name", "age", "email", "department"):
                setattr(student, key, value)

        return student

    return None


def delete_student(student_id):
    student = get_student(student_id)

    if student:
        students.remove(student)
        return True

    return False