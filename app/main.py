from fastapi import FastAPI

from app.database.database import Base, engine
from app.database import orm_models

from app.api.student_routes import router as student_router
from app.api.faculty_routes import router as faculty_router
from app.api.course_routes import router as course_router
from app.api.enrollment_routes import router as enrollment_router

from app.services.database_service import get_database_summary


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusHub ERP",
    description="College Management System",
    version="1.0.0"
)


app.include_router(student_router)
app.include_router(faculty_router)
app.include_router(course_router)
app.include_router(enrollment_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CampusHub ERP",
        "status": "Running successfully"
    }


@app.get("/summary")
def database_summary():
    return get_database_summary()