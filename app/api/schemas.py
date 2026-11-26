from pydantic import BaseModel, Field, ConfigDict
class ValidatedSchema(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )


class StudentSchema(ValidatedSchema):
    student_id: str = Field(pattern=r"^ST[0-9]{3,}$")
    name: str = Field(min_length=1)
    age: int = Field(ge=16, le=80)
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    department: str = Field(min_length=1)


class FacultySchema(ValidatedSchema):
    faculty_id: str = Field(pattern=r"^FC[0-9]{3,}$")
    name: str = Field(min_length=1)
    age: int = Field(ge=16, le=80)
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    department: str = Field(min_length=1)


class CourseSchema(ValidatedSchema):
    course_id: str = Field(pattern=r"^CS[0-9]{3,}$")
    course_name: str = Field(min_length=1)
    credits: int = Field(gt=0)
    faculty_id: str = Field(pattern=r"^FC[0-9]{3,}$")


class EnrollmentSchema(ValidatedSchema):
    enrollment_id: str = Field(pattern=r"^EN[0-9]{3,}$")
    student_id: str = Field(pattern=r"^ST[0-9]{3,}$")
    course_id: str = Field(pattern=r"^CS[0-9]{3,}$")