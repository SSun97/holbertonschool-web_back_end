#!/usr/bin/env python3
""" type-annotated function sum_list """


def sum_list(input_list) -> float:
    """ Doc """
    sum: float = 0
    for item in input_list:
        sum += item
    return float(sum)
