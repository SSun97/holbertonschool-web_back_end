#!/usr/bin/env python3
""" Write a function called filter_datum that
returns the log message obfuscated: """

from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ returns the log messages obfuscated """
    for info in fields:
        message = re.sub(f'{info}=.+?{separator}',
                         f'{info}={redaction}{separator}',
                         message)
    return message
