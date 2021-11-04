#!/usr/bin/env python3
""" Write a coroutine called async_generator that takes no arguments. """


import random
import asyncio
from typing import Generator

async def async_generator() -> Generator[int, None, None]:
    """ Doc """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
