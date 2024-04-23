#!/usr/bin/env python3
'''comprehension'''
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    '''returns list'''
    async_generator = __import__('0-async_generator').async_generator
    asyn: List = [asyn async for asyn in async_generator()]
    return asyn
