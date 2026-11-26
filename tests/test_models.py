import pytest

from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


def test_create_student():
    student = Student(
        "ST001", "Rahul", 20, "rahul@gmail.com", "CS"
    )

    assert student.student_id == "ST001"
    assert student.name == "Rahul"
    assert student.age == 20


def test_invalid_student_name():
    with pytest.raises(ValueError):
        Student("ST001", "", 20, "rahul@gmail.com", "CS")


def test_invalid_student_age():
    with pytest.raises(ValueError):
        Student("ST001", "Rahul", 10, "rahul@gmail.com", "CS")


def test_invalid_student_email():
    with pytest.raises(ValueError):
        Student("ST001", "Rahul", 20, "invalidemail", "CS")


def test_student_to_dict():
    student = Student(
        "ST001", "Rahul", 20, "rahul@gmail.com", "CS"
    )

    assert student.to_dict() == {
        "student_id": "ST001",
        "name": "Rahul",
        "age": 20,
        "email": "rahul@gmail.com",
        "department": "CS"
    }


def test_create_faculty():
    faculty = Faculty(
        "FC001", "Amit", 35, "amit@gmail.com", "CS"
    )

    assert faculty.faculty_id == "FC001"
    assert faculty.name == "Amit"
    assert faculty.age == 35


def test_invalid_faculty_email():
    with pytest.raises(ValueError):
        Faculty("FC001", "Amit", 35, "invalidemail", "CS")


def test_create_course():
    course = Course(
        "CS001", "Python Programming", 4, "FC001"
    )

    assert course.course_id == "CS001"
    assert course.course_name == "Python Programming"
    assert course.credits == 4
    assert course.faculty_id == "FC001"