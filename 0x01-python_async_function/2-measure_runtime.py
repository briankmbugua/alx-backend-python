#!/usr/bin/env python3
"""Measure the runtime
"""


import time
import asyncio
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime
    """
    start_time = time.time()

    async def measure_wait_n():
        await wait_n(n, max_delay)
    asyncio.run(measure_wait_n())
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
