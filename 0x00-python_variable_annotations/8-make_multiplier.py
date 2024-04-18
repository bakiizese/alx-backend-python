#!/usr/bin/env python3
'''annptated'''
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''call recurse to mult'''
    def f(n: float) -> float:
        ''''recurse'''
        return float(n * multiplier)
    return f
