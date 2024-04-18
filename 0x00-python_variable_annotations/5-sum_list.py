#!/usr/bin/env python3
from typing import List
'''list annoated'''


def sum_list(input_list: List[float]) -> float:
    '''sum_list'''
    j = 0
    for i in input_list:
        j += i
    return j
