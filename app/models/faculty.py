from app.core.abc_interfaces import Person
from app.core.descriptors import NameDescriptor, EmailDescriptor, AgeDescriptor
from app.core.metaclasses import ModelMeta


class Faculty(Person, metaclass=ModelMeta):

    name = NameDescriptor()
    email = EmailDescriptor()
    age = AgeDescriptor()

    def __init__(self, faculty_id, name, age, email, department):
        self.faculty_id = faculty_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department

    def display_details(self):
        print("Faculty ID:", self.faculty_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Department:", self.department)

    def to_dict(self):
        return {
            "faculty_id": self.faculty_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department
        }