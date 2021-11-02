#!/usr/bin/env python3
""" type-annotated function make_multiplier """


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ Doc """
    def multiply(n: float) -> float:
        return multiplier * n
    return multiply
