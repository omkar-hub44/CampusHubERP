import asyncio

from app.services.database_service import (
    get_student_objects,
    get_faculty_objects,
    get_course_objects,
    get_enrollment_objects
)

from app.services.report_service import (
    generate_student_report,
    generate_faculty_report,
    generate_course_report,
    generate_enrollment_report
)


async def load_students():
    return await asyncio.to_thread(get_student_objects)


async def load_faculty():
    return await asyncio.to_thread(get_faculty_objects)


async def load_courses():
    return await asyncio.to_thread(get_course_objects)


async def load_enrollments():
    return await asyncio.to_thread(get_enrollment_objects)


async def load_all_data():

    students, faculty, courses, enrollments = await asyncio.gather(
        load_students(),
        load_faculty(),
        load_courses(),
        load_enrollments()
    )

    return {
        "students": students,
        "faculty": faculty,
        "courses": courses,
        "enrollments": enrollments
    }


async def generate_reports_async(
    students, faculty, courses, enrollments
):

    await asyncio.gather(
        asyncio.to_thread(generate_student_report, students),
        asyncio.to_thread(generate_faculty_report, faculty),
        asyncio.to_thread(generate_course_report, courses),
        asyncio.to_thread(generate_enrollment_report, enrollments)
    )

    print("All asynchronous reports generated successfully")