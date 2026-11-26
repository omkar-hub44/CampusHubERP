from app.utils.logger import logger


class Repository:

    def __init__(self, db, model):
        self.db = db
        self.model = model

    def create(self, data):
        record = self.model(**data)

        try:
            self.db.add(record)
            self.db.commit()
            self.db.refresh(record)

            logger.info(
                f"{self.model.__name__} record created successfully"
            )

            return record

        except Exception:
            self.db.rollback()
            logger.exception(
                f"Error creating {self.model.__name__} record"
            )
            raise

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_id(self, record_id):
        return self.db.get(self.model, record_id)

    def update(self, record_id, data):
        record = self.get_by_id(record_id)

        if record is None:
            logger.warning(
                f"{self.model.__name__} record not found"
            )
            return None

        try:
            for key, value in data.items():
                setattr(record, key, value)

            self.db.commit()
            self.db.refresh(record)

            logger.info(
                f"{self.model.__name__} record updated successfully"
            )

            return record

        except Exception:
            self.db.rollback()
            logger.exception(
                f"Error updating {self.model.__name__} record"
            )
            raise

    def delete(self, record_id):
        record = self.get_by_id(record_id)

        if record is None:
            logger.warning(
                f"{self.model.__name__} record not found"
            )
            return False

        try:
            self.db.delete(record)
            self.db.commit()

            logger.info(
                f"{self.model.__name__} record deleted successfully"
            )

            return True

        except Exception:
            self.db.rollback()
            logger.exception(
                f"Error deleting {self.model.__name__} record"
            )
            raise