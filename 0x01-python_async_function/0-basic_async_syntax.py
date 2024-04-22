#!/usr/bin/env python3
import asyncio
import random
'''async await with random'''


async def wait_random(max_delay=10: int) -> float:
    '''await random num'''
    r = random.uniform(0, 10)
    await asyncio.sleep(r)
    return r
