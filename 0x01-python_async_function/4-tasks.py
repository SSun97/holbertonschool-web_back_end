#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in 2 integer arguments  """

import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """ Doc arr is the list of objects wait_random returned """
    arr = []
    arr1 = []
    for x in range(n):
        arr.append(task_wait_random(max_delay))
    for item in asyncio.as_completed(arr):
        arr1.append(await item)
    return arr1
