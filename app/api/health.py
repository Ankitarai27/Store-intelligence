from datetime import UTC
from datetime import datetime

from fastapi import APIRouter

from app.db.health import validate_database_connection

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check() -> dict:
    database_status = validate_database_connection()

    return {
        "status": (
            "healthy"
            if database_status.healthy
            else "degraded"
        ),
        "service": "store-intelligence-api",
        "database": {
            "healthy": database_status.healthy,
            "message": database_status.message,
        },
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }