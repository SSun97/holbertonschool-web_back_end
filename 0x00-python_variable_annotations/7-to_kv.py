#!/usr/bin/env python3
""" type-annotated function to_kv """


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ Doc """
    return (k, pow(v, 2))
