#!/usr/bin/env python3
""" Write a function called filter_datum that
returns the log message obfuscated: """

from typing import List
import re
import logging
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')
""" important PIIs or information that you must hide in your logs """

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ init constructor """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values in incoming log records """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


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


def get_logger() -> logging.Logger:
    """ takes no arguments returns a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
