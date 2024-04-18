#!/usr/bin/env python3
from typing import List, Union
'''mixed list annotated'''


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''sum mixed'''
    sm = 0.0
    for i in mxd_lst:
        sm += i
    return sm
