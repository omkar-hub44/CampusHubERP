def student_generator(students):
    for student in students:
        yield student


def faculty_generator(faculty_members):
    for faculty in faculty_members:
        yield faculty


def course_generator(courses):
    for course in courses:
        yield course