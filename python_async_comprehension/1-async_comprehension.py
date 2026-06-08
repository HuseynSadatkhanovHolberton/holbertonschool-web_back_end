#!/usr/bin/env python3
"""
Module containing the async_comprehension coroutine.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator
    using an asynchronous comprehension.

    Returns:
        List[float]: A list of 10 random float values.
    """
    return [number async for number in async_generator()]
