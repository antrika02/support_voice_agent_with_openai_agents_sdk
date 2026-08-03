import time

from fastapi import FastAPI, Request

from app.logging import get_logger


logger = get_logger(__name__)


def register_timing_middleware(app: FastAPI) -> None:
    """
    Measure execution time of every request.
    """

    @app.middleware("http")
    async def add_timing(request: Request, call_next):

        start = time.perf_counter()

        response = await call_next(request)

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"took {elapsed:.2f} ms"
        )

        response.headers[
            "X-Process-Time"
        ] = f"{elapsed:.2f} ms"

        return response