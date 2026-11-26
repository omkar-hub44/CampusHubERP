from threading import Lock

from app.database.database import engine, SessionLocal


class DatabaseManager:

    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

        return cls._instance

    def get_engine(self):
        return engine

    def get_session(self):
        return SessionLocal()