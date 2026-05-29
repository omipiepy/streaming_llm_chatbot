import asyncio


async def run_with_timeout(coro, timeout: float):
    return await asyncio.wait_for(coro, timeout=timeout)