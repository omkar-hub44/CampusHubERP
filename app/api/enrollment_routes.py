from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.database import get_db
from app.services.database_service import DatabaseService
from app.api.schemas import EnrollmentSchema
from app.database.orm_models import EnrollmentORM


router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("/", status_code=201)
def add_enrollment(
    enrollment: EnrollmentSchema,
    db: Session = Depends(get_db)
):
    service = DatabaseService(db)

    if service.students.get_by_id(enrollment.student_id) is None:
        raise HTTPException(status_code=404, detail="Student not found")

    if service.courses.get_by_id(enrollment.course_id) is None:
        raise HTTPException(status_code=404, detail="Course not found")

    existing = db.query(EnrollmentORM).filter_by(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Student is already enrolled in this course"
        )

    data = enrollment.model_dump()
    data["enrollment_date"] = datetime.now().isoformat()

    try:
        return service.enrollments.create(data)
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Enrollment could not be created"
        )


@router.get("/")
def get_all_enrollments(db: Session = Depends(get_db)):
    service = DatabaseService(db)
    return service.enrollments.get_all()


@router.get("/{enrollment_id}")
def get_enrollment(
    enrollment_id: str,
    db: Session = Depends(get_db)
):
    service = DatabaseService(db)
    enrollment = service.enrollments.get_by_id(enrollment_id)

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


@router.put("/{enrollment_id}")
def update_enrollment(
    enrollment_id: str,
    enrollment: EnrollmentSchema,
    db: Session = Depends(get_db)
):
    service = DatabaseService(db)

    if enrollment_id != enrollment.enrollment_id:
        raise HTTPException(
            status_code=400,
            detail="Enrollment ID cannot be changed"
        )

    if service.enrollments.get_by_id(enrollment_id) is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    if service.students.get_by_id(enrollment.student_id) is None:
        raise HTTPException(status_code=404, detail="Student not found")

    if service.courses.get_by_id(enrollment.course_id) is None:
        raise HTTPException(status_code=404, detail="Course not found")

    existing = db.query(EnrollmentORM).filter(
        EnrollmentORM.student_id == enrollment.student_id,
        EnrollmentORM.course_id == enrollment.course_id,
        EnrollmentORM.enrollment_id != enrollment_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Student is already enrolled in this course"
        )

    try:
        return service.enrollments.update(
            enrollment_id,
            enrollment.model_dump(exclude={"enrollment_id"})
        )
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Enrollment could not be updated"
        )


@router.delete("/{enrollment_id}")
def delete_enrollment(
    enrollment_id: str,
    db: Session = Depends(get_db)
):
    service = DatabaseService(db)

    if not service.enrollments.delete(enrollment_id):
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return {"message": "Enrollment deleted successfully"}