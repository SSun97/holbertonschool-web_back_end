#!/usr/bin/env python3
""" write a measure_runtime coroutine that will execute
async_comprehension four times """


from typing import List
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Doc """
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         )
    end_time = time.time()
    return (end_time - start_time)
