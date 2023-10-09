#!/usr/bin/env python3
'''Callable
'''
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
