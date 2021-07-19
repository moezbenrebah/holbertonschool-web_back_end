#!/usr/bin/env python3

"""
This is the "6-sum_mixed_list" module.
The 6-sum_mixed_list module function:
sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list: takes a list of floats and integers and return the sum.

    Args:
        mxd_lst (List): a list of floats and integers
    Return:
        float
    """
    return sum(mxd_lst)
