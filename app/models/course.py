from app.core.metaclasses import ModelMeta


class Course(metaclass=ModelMeta):

    def __init__(self, course_id, course_name, credits, faculty_id):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.faculty_id = faculty_id

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "credits": self.credits,
            "faculty_id": self.faculty_id
        }