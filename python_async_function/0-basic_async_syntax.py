#!/usr/bin/env python3
"""This module containts asyncious wait_random function."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function takes max_delay value then randomly choose number
    from 0 to max_delay, whaits for that period and then returns that value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
