from fastapi import FastAPI, Request

from app.logging import get_logger


logger = get_logger(__name__)


def register_request_logging(app: FastAPI) -> None:
    """
    Logs every incoming HTTP request and response.
    """

    @app.middleware("http")
    async def log_request(request: Request, call_next):

        logger.info(
            f"{request.method} {request.url.path} started."
        )

        response = await call_next(request)

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"completed "
            f"({response.status_code})"
        )

        return response