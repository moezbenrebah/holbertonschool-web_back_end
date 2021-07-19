#!/usr/bin/env python3
"""
This is the "9-element_length" module.
The 9-element_length module function:
element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int].
"""

from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length: takes an iterable object and returns
    the length of each element.

    Args:
        lst (Iterable): object
    Return:
        integer
    """
    return [(i, len(i)) for i in lst]
