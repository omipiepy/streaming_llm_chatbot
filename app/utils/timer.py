import asyncio
import time

from app.core.logger import setup_logging, get_logger

setup_logging()

logger = get_logger(__name__)
logger.info("Timer utility initialized")


async def run_with_timeout(coro, timeout: int):
    start = time.time()

    try:
        logger.info(
            f"Running task with timeout of {timeout} seconds..."
        )

        result = await asyncio.wait_for(
            coro,
            timeout=timeout
        )

        return result

    except asyncio.TimeoutError as e:
        elapsed = time.time() - start

        message = (
            f"Timeout after {elapsed:.2f}s "
            f"(limit={timeout}s)"
        )

        logger.error(message)

        raise TimeoutError(message) from e