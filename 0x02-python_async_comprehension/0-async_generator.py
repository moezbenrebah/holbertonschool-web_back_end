#!/usr/bin/env python3
"""async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
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
