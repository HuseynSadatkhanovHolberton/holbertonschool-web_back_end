#!/usr/bin/env python3
"""
Module containing the task_wait_n coroutine.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns
    the delays in ascending order.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: Delays ordered by completion time.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)

    return delays
