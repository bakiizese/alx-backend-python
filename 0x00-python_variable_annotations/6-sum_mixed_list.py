#!/usr/bin/env python3
'''mixed list annotated'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''sum mixed'''
    sm = 0.0
    for i in mxd_lst:
        sm += i
    return sm
