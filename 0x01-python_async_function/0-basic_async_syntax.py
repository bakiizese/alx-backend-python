#!/usr/bin/env python3
'''async await with random'''
import random
import asyncio


async def wait_random(max_delay=10):
    '''await random num'''
    r = random.uniform(0, 10)
    await asyncio.sleep(r)
    return r
