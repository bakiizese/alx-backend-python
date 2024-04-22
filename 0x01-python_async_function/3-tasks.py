#!/usr/bin/env python3
'''asyncio tasks'''
from asyncio import Task
import asyncio


def task_wait_random(max_delay: int) -> Task:
    '''creating tasks'''
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
