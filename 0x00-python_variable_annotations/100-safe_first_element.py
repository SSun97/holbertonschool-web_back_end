#!/usr/bin/env python3
""" type-annotated function duck-typed """


import types
import typing

Nonetype = type(None)


def safe_first_element(lst: typing.Sequence[typing.Any]) ->\
        typing.Union[typing.Any, Nonetype]:
    if lst:
        return lst[0]
    else:
        return None
