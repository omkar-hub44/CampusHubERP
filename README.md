
# CampusHub ERP

## Project Overview

CampusHub ERP is a Python-based College Management System
developed as an Advanced Python OJT project.

The system manages students, faculty, courses and enrollments
using REST APIs and a SQLite database.

## Features

- Student Management
- Faculty Management
- Course Management
- Enrollment Management
- CRUD Operations
- Input Validation
- JSON Import and Export
- Report Generation
- Multithreading and Multiprocessing
- Asynchronous Programming
- Application Logging
- Automated Testing
- REST API Documentation

## Technologies Used

- Python 3.14
- FastAPI
- SQLite
- SQLAlchemy ORM
- Pydantic
- Uvicorn
- Pytest
- Swagger UI

## Design Patterns

- Singleton Pattern
- Factory Pattern
- Repository Pattern

## Installation

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment on Windows:

    .venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

## Initialize Sample Data

    python -m app.database.seed_data

## Run the Application

    python -m uvicorn app.main:app --reload

Application URL:

http://127.0.0.1:8000

Swagger API Documentation:

http://127.0.0.1:8000/docs

## Run Automated Tests

    python -m pytest tests -v

## Project Structure

- app/core - OOP concepts and design patterns
- app/models - Domain models
- app/services - Business logic
- app/utils - Utility functions
- app/database - Database configuration and repository
- app/api - REST API routes and schemas
- data - JSON data files
- reports - Generated reports
- logs - Application logs
- tests - Automated test cases

## Current Limitations

- JSON import reads records but does not restore them into SQLite.
- The application provides REST APIs and Swagger UI rather than
  a graphical frontend.

## Conclusion

CampusHub ERP demonstrates advanced Python programming,
database management, REST API development, concurrency,
design patterns, validation, logging and automated testing.
