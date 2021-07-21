#!/usr/bin/env python3
"""creating Task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    task_wait_random: takes an integer max_delay and return
    Task object

    Args:
        max_delay (int): a random delay
    Return:
        Task object
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
