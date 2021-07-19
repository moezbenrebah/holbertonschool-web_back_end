#!/usr/bin/env python3
"""
This is the "8-make_multiplier" module.
The 8-make_multiplier module function:
make_multiplier(multiplier: float) -> Callable[[float], float].
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier: takes a float and returns a function that multiply
    a float with multiplier.

    Args:
        multiplier (float): a float
    Return:
        function
    """
    return lambda a: multiplier*a
