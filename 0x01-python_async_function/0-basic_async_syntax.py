#!/usr/bin/env python3
'''async await with random'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''wait rand'''
    r: float = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
