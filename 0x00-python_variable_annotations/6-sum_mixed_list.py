#!/usr/bin/env python3
""" type-annotated function sum_mixed_list """


import typing


Mxd_list = typing.List[typing.Union[int, float]]


def sum_mixed_list(mxd_lst: Mxd_list) -> float:
    """ Doc """
    sum: float = 0
    for item in mxd_lst:
        sum += item
    return float(sum)
