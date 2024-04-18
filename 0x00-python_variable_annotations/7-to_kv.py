#!/usr/bin/env python3
''' tuple annotated '''
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''tuple'''
    return (k, v**2)
