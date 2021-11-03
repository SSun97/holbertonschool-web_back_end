#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in 2 integer arguments  """

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """ Doc """
    arr = []
    arr1 = []
    for x in range(n):
        arr.append(wait_random(max_delay))
    for item in asyncio.as_completed(arr):
        arr1.append(await item)
    return arr1
