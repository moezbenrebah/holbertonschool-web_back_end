#!/usr/bin/env python3
"""
This is the "7-to_kv" module.
The 7-to_kv module function:
to_kv(k: str, v: Union[int, float]) -> Tuple[str, float].
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: takes a string k an int OR float v and return a tuple.

    Args:
        k (str): a string
        v (int OR float): integer or float
    Return:
        tuple
    """
    return (k, v**2)
