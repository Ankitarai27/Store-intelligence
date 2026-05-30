from datetime import UTC
from datetime import datetime

from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check() -> dict:
    return {
        "status": "healthy",
        "service": "store-intelligence-api",
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }