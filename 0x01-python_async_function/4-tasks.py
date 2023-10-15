#!/usr/bin/env python3
"""task_wait_random
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
