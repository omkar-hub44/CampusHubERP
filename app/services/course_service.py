from app.models.course import Course

courses = []


def add_course(course):
    courses.append(course)
    return course


def get_all_courses():
    return courses


def get_course(course_id):
    for course in courses:
        if course.course_id == course_id:
            return course
    return None


def update_course(course_id, **kwargs):
    course = get_course(course_id)

    if course:
        for key, value in kwargs.items():
            if key in ("course_name", "credits", "faculty_id"):
                setattr(course, key, value)

        return course

    return None


def delete_course(course_id):
    course = get_course(course_id)

    if course:
        courses.remove(course)
        return True

    return False