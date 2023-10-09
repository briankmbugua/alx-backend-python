#!/usr/bin/env python3
'''Calculate the sum of a list of integers and floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Calculate the sum of a list of integers and floats
    '''
    return float(sum(mxd_lst))
