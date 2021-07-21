#!/usr/bin/env python3
"""measure runtime"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime: takes 0 arguments and measure
    the total runtime and return it

    Return:
        float
    """

    t = perf_counter()

    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)

    total_time = perf_counter() - t

    return total_time
