from dataclasses import dataclass

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine


@dataclass(slots=True)
class DatabaseHealthResult:
    healthy: bool
    message: str


def validate_database_connection() -> DatabaseHealthResult:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return DatabaseHealthResult(
            healthy=True,
            message="database connection successful",
        )

    except SQLAlchemyError as exc:
        return DatabaseHealthResult(
            healthy=False,
            message=str(exc),
        )