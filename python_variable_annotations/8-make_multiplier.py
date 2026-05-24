#!/usr/bin/env python3
"""This module contains make_multinplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function takes float and returns another function.
    """
    def multiplying(n: float) -> float:
        """
        Function multiplies a float by multiplier.
        """
        return n * multiplier
    
    return multiplying
