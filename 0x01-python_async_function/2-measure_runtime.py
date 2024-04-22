#!/usr/bin/env python3
'''time elapsed'''
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    '''measrue time'''
    async def measure():
        '''ascync def'''
        wait_n = __import__('1-concurrent_coroutines').wait_n
        start_tim: float = time.time()
        await wait_n(n, max_delay)
        end_time: float = time.time()

        return end_time - start_tim
    return asyncio.run(measure())
