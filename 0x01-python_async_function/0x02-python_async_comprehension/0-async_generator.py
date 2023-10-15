#!/usr/bin/env python3

import asyncio
import random
from typing import Generator
"""ASYNC GENERATOR"""


async def async_generator() -> Generator[float, None, None]:
    """Yield a random number between 0 and 10 every second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
