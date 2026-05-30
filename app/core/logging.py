import logging
import sys

import structlog

from app.core.config import get_settings


def configure_logging() -> None:
    settings = get_settings()

    numeric_level = getattr(
        logging,
        settings.log_level.upper(),
        logging.INFO,
    )

    logging.basicConfig(
        level=numeric_level,
        format="%(message)s",
        stream=sys.stdout,
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            numeric_level
        ),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )