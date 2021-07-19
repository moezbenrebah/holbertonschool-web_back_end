#!/usr/bin/env python3
"""
This is the "101-safely_get_value" module.
The 101-safely_get_value module function:
safely_get_value(dct: Mapping,
                 key: Any,
                 default: Union[T, None]) -> Union[Any, T].
"""
from typing import TypeVar, Any, Union, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    safely_get_value: returns values of each parameter.

    Args:
        dct (dict): a dictionary
        key (Any): any type
        default: any type
    Return:
        any type
    """
    if key in dct:
        return dct[key]
    else:
        return default
