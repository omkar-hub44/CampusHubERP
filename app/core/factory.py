from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course
from app.models.enrollment import Enrollment


class ModelFactory:

    @staticmethod
    def create_model(model_type, **kwargs):

        models = {
            "student": Student,
            "faculty": Faculty,
            "course": Course,
            "enrollment": Enrollment
        }

        model_class = models.get(model_type.lower())

        if model_class is None:
            raise ValueError("Invalid model type")

        return model_class(**kwargs)