#!/usr/bin/env python3
"""This module contains element_lenght function."""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function takes iterable sequence and return list of tuple of suquence.
    """
    return [(i, len(i)) for i in lst]
