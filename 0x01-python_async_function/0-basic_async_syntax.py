#!/usr/bin/env python3
"""asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: take an integer with a value of 10 and await for
    a rondom delay.

    Args:
        max_delay (int): integer

    Return:
        a random float
    """
    a = random.uniform(0, max_delay)
    await asyncio.sleep(a)

    return a
