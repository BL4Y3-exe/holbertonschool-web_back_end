#!/usr/bin/env python3
"""This module contains asyncinous function wait_n."""
import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function takes n and max_delay
    and returns the list of all delays.
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = []
    for task in asincio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
