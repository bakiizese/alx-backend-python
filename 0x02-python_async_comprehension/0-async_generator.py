#!/usr/bin/env python3
'''comprehension'''
import asyncio
import random
from typing import List


async def async_generator(): -> List[float]:
    '''generator'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
