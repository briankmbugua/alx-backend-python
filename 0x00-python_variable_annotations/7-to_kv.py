#!/usr/bin/env python3
'''Create a tuple with the string k and the square of int/float v.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Create a tuple with the string k and the square of int/float v.
    '''
    return (k, float(v**2))
