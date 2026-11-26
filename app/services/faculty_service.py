from app.models.faculty import Faculty

faculty_members = []


def add_faculty(faculty):
    faculty_members.append(faculty)
    return faculty


def get_all_faculty():
    return faculty_members


def get_faculty(faculty_id):
    for faculty in faculty_members:
        if faculty.faculty_id == faculty_id:
            return faculty
    return None


def update_faculty(faculty_id, **kwargs):
    faculty = get_faculty(faculty_id)

    if faculty:
        for key, value in kwargs.items():
            if key in ("name", "age", "email", "department"):
                setattr(faculty, key, value)

        return faculty

    return None


def delete_faculty(faculty_id):
    faculty = get_faculty(faculty_id)

    if faculty:
        faculty_members.remove(faculty)
        return True

    return False