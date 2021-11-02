#!/usr/bin/env python3
""" type-annotated function duck-typed """


from types import NoneType
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) ->\
                            typing.Union[typing.Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
