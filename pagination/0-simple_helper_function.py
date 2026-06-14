#!/usr/bin/env python3
"""This module contains index_range function."""


def index_range(page, page_size):
    """
    Function returns a tuple of start and end indexes for pagination.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
