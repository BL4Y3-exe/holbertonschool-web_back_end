#!/usr/bin/env python3
"""This module contains measure_time function."""
from asyncio import run
from time import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function mesures the total execution time for wait_n(n, max_delay)
    and returns total_time/n.
    """
    start_time = time()
    
    run(wait_n(n, max_delay))
    
    end_time = time()
    
    total_time = end_time - start_time
    
    return total_time / n