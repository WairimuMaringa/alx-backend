#!/usr/bin/env python3
"""
Function that takes two integer args and returns a tuple
of size two containing a start and end indexes
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return tuple. """
    return ((page - 1) * page_size, page * page_size)
