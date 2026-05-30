from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.events import router as events_router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.middleware.request_logging import RequestLoggingMiddleware


configure_logging()

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(health_router)
app.include_router(events_router)

@app.get("/")
async def root() -> dict:
    return {
        "message": "Store Intelligence API",
        "environment": settings.app_env,
    }