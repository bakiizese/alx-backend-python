#!/usr/bin/env python3
'''multi coroutines'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''multi'''
    coroutines: List = [wait_random(max_delay) for _ in range(n)]
    rlist: List[float] = await asyncio.gather(*coroutines)

    return sorted(rlist)
