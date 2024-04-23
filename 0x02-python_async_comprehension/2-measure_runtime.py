#!/usr/bin/env python3
'''time measurement'''
import asyncio
import time


def measure_runtime() -> float:
    '''measure'''
    async def measure() -> float:
        '''measure'''
        async_c = __import__('1-async_comprehension').async_comprehension
        st_time: float = time.time()
        await asyncio.gather(async_c(), async_c(),
                             async_c(), async_c())
        st_end: float = time.time()

        return st_end - st_time
    return measure()
