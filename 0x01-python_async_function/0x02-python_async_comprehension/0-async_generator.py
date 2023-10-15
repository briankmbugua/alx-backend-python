#!/usr/bin/env python3

import asyncio
import random
"""ASYNC GENERATOR"""


async def async_generator():
    """Yield a random float between 0 and 10 every second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
