#!/usr/bin/env python3
"""
This is the "5-sum_list" module.
The 5-sum_list module function: sum_list(input_list: List[float]) -> float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list: takes a list of floats and returns their sum as a float.

    Args:
        input_list (List): a list of floats
    Return:
        float
    """
    return sum(input_list)
