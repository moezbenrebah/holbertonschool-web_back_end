#!/usr/bin/env python3
"""asynchronous coroutine"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time: takes 2 arguments and return the measures
    of the total execution time for wait_n function

    Args:
        n (int): integer
        max_delay (int) : integer
    Return:
        a float
    """
    t = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - t
    return total_time / n
