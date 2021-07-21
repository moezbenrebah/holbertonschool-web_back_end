#!/usr/bin/env python3
"""asychronous coroutine"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
    async_generator: takes no arguments and return
    a random float number

    Return:
        list of floats
    """
    n = 10
    for i in range(n):
        x = random.uniform(i, n)
        yield(x)
        await asyncio.sleep(1)
