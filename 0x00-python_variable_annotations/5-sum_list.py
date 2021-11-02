#!/usr/bin/env python3
""" type-annotated function sum_list """


import typing


Input_list = typing.List[float]


def sum_list(input_list: Input_list) -> float:
    """ Doc """
    sum: float = 0
    for item in input_list:
        sum += item
    return float(sum)
