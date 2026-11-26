def get_student_names(students):
    return list(map(lambda student: student.name, students))


def filter_by_department(students, department):
    return list(
        filter(lambda student: student.department == department, students)
    )


def sort_students_by_name(students):
    return sorted(students, key=lambda student: student.name)


def sort_students_by_age(students):
    return sorted(students, key=lambda student: student.age)