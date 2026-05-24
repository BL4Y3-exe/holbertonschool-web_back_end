#!/usr/bin/env python3
"""This module contains "sum_list" type-annotated function."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function takes list of floats and returns their sum.
    """
    return sum(input_list)
