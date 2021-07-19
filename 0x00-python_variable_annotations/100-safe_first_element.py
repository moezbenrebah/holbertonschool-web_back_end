#!/usr/bin/env python3
"""
This is the "100-safe_first_element" module.
The 100-safe_first_element module function:
safe_first_element(lst: Sequence[Any]) -> Union[Any, None].
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element: takes a sequence of any type of elements and returns
    the first element.

    Args:
        lst (Any): any type
    Return:
        element type
    """
    if lst:
        return lst[0]
    else:
        return None
