from sqlalchemy import Column, String, Integer, ForeignKey, Index
from app.database.database import Base


class StudentORM(Base):

    __tablename__ = "students"

    student_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)


class FacultyORM(Base):

    __tablename__ = "faculty"

    faculty_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)


class CourseORM(Base):

    __tablename__ = "courses"

    course_id = Column(String, primary_key=True)
    course_name = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)

    faculty_id = Column(
        String, ForeignKey("faculty.faculty_id"),
        nullable=False
    )


class EnrollmentORM(Base):

    __tablename__ = "enrollments"

    __table_args__ = (
        Index(
            "uq_student_course",
            "student_id",
            "course_id",
            unique=True
        ),
    )

    enrollment_id = Column(String, primary_key=True)

    student_id = Column(
        String, ForeignKey("students.student_id"),
        nullable=False
    )

    course_id = Column(
        String, ForeignKey("courses.course_id"),
        nullable=False
    )

    enrollment_date = Column(String, nullable=False)