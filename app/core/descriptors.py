class NameDescriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._name

    def __set__(self, instance, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")

        instance._name = value


class EmailDescriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._email

    def __set__(self, instance, value):
        if "@" not in value:
            raise ValueError("Email must contain @")

        instance._email = value


class AgeDescriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._age

    def __set__(self, instance, value):
        if not isinstance(value, int) or not 16 <= value <= 80:
            raise ValueError("Age must be between 16 and 80")

        instance._age = value

