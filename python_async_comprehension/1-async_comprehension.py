#!/usr/bin/env python3
"""This module contains async_comperhension coroutine."""
import asyncio
from typing import List

async_generator = __import__('5-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension

    over async_generator, then returns the 10 random numbers.
    """

    return [number async for number in async_generator()]
