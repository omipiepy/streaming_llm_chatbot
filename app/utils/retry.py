import asyncio
import httpx
from app.core.logger import setup_logging, get_logger

setup_logging()

logger = get_logger(__name__)
logger.info("Retry utility initialized")


async def retry_async(func, max_attempts=3, delay=2):

    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            return await func()

        except (httpx.TimeoutException, httpx.ConnectError) as e:
            last_error = e
            logger.warning(f"Attempt {attempt} failed with error: {e}")
            print(f"[Retry {attempt}/{max_attempts}] {e}")

            if attempt < max_attempts:
                await asyncio.sleep(delay)

        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt}: {e}")
            raise e
        

    raise RuntimeError(f"All retries failed: {last_error}")