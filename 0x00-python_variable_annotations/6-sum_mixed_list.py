#!/usr/bin/env python3
'''mixed list annotated'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''sum mixed'''
    return float(sum(mxd_lst))
