#!/usr/bin/env python3
"""This module contains to_kv function."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function takes str and decimal and returns them in tuple.
    """
    return k, float(v**2)
