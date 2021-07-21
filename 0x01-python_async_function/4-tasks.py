#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n: takes 2 arguments n and max_delay and return
    list of all the delays(float values).
    Args:
        n (int): integer
        max_delay (int): integer
    Return:
        a list of floats
    """

    a = [task_wait_random(max_delay) for i in range(n)]

    spawn = []
    for i in asyncio.as_completed(a):
        res = await i
        spawn.append(res)

    return spawn
