from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.logging import get_logger


logger = get_logger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers.
    """

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(
            "Unhandled exception occurred."
        )

        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error."
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        logger.warning(
            "Validation error."
        )

        return JSONResponse(
            status_code=422,
            content={
                "detail": exc.errors()
            },
        )