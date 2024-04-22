#!/usr/bin/env python3
'''multi coroutines'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''multi'''
    coroutines: List = [task_wait_random(max_delay) for _ in range(n)]
    rlist: List[float] = await asyncio.gather(*coroutines)

    return sorted(rlist)
