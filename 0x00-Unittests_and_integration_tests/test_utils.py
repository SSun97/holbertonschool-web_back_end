#!/usr/bin/env python3
""" unitest and unitest.mock """
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class for test purpose """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test function acces_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test function acces_nested_map when Error raised """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        print(error.exception.args)
        self.assertEqual(error.exception.args[0], path[-1])

