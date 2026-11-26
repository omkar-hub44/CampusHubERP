from concurrent.futures import ProcessPoolExecutor


def count_records(records):
    return len(records)


def calculate_totals(students, faculty_members, courses, enrollments):

    with ProcessPoolExecutor(max_workers=4) as executor:

        student_task = executor.submit(count_records, students)
        faculty_task = executor.submit(count_records, faculty_members)
        course_task = executor.submit(count_records, courses)
        enrollment_task = executor.submit(count_records, enrollments)

        return {
            "total_students": student_task.result(),
            "total_faculty": faculty_task.result(),
            "total_courses": course_task.result(),
            "total_enrollments": enrollment_task.result()
        }