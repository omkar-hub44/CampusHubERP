from datetime import datetime
from app.core.metaclasses import ModelMeta


class Enrollment(metaclass=ModelMeta):

    def __init__(self, enrollment_id, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = datetime.now().isoformat()

    def to_dict(self):
        return {
            "enrollment_id": self.enrollment_id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "enrollment_date": self.enrollment_date
        }