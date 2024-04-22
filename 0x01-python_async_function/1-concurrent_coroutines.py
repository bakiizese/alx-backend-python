#!/usr/bin/env python3
'''multi coroutines'''
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> float:
    '''multi'''
    wait_random = __import__('0-basic_async_syntax').wait_random
    coroutines: List = [wait_random(max_delay) for _ in range(n)]
    rlist: List[float] = await asyncio.gather(*coroutines)

    return sorted(rlist)
