#!/usr/bin/env python3
"""Generic type for a function"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
 dict: Mapping,
 key: Any,
 default: Union[T, None] = None
 ) -> Union[Any, T]:
    """Generic type for a function"""
    if key in dct:
        return dct[key]
    else:
        return default
