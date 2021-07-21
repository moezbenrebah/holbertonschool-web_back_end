#!/usr/bin/env python3
"""async comprehension"""

import asyncio
from typing import List
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension: takes no arguments, it returns the 10 random numbers
    after collect 10 random numbers from 'async_generator' function

    Return:
        a list of flots
    """
    a = [i async for i in async_generator()]
    return a
