#!/usr/bin/env python3
"""
Module containing the wait_n coroutine.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the delays in ascending order.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: Delays returned by the coroutines,
        ordered by completion time.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)

    return delays
