#!/usr/bin/env python3
""" Write a function called filter_datum that
returns the log message obfuscated: """

from typing import List
import re
import logging
import os
import mysql.connector
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns a connector to the database """
    return mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))


def main():
    """ The function will obtain a database connection using get_db and
    retrieve all rows in the users table and display each row under a
    filtered format """
    dbObj = get_db()
    cursor = dbObj.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    for row in cursor:
        record = ''
        i = 0
        for header in cursor.column_names:
            record += f"{header}={row[i]}; "
            i += 1
        log_record = logging.LogRecord("user_data", logging.INFO,
                                       None, None, record, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        print(formatter.format(log_record))
    cursor.close()
    dbObj.close()


if __name__ == "__main__":
    main()
