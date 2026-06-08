#!/usr/bin/env python3
"""
Module for measuring the runtime of wait_n.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time per coroutine.

    Args:
        n (int): Number of coroutines.
        max_delay (int): Maximum delay.

    Returns:
        float: Total execution time divided by n.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    return (end_time - start_time) / n
