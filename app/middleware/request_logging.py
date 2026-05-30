import time
import uuid

import structlog
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


logger = structlog.get_logger()


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        trace_id = str(uuid.uuid4())

        start_time = time.perf_counter()

        response = await call_next(request)

        latency_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2,
        )

        logger.info(
            "request_completed",
            trace_id=trace_id,
            method=request.method,
            path=request.url.path,
            latency_ms=latency_ms,
            status_code=response.status_code,
        )

        response.headers["X-Trace-ID"] = trace_id

        return response