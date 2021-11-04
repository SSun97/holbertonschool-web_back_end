#!/usr/bin/env python3
""" write a coroutine called async_comprehension that takes no arguments """


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Doc """
    return [i async for i in async_generator()]
