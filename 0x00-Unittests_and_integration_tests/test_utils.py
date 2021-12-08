#!/usr/bin/env python3
""" unitest and unitest.mock """
from parameterized import parameterized
import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize


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
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ class for testing get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get_json):
        """ test get json function, mock path where function is used """
        mock_get_json.return_value = test_payload
        expected = get_json(test_url)
        self.assertEqual(expected, test_payload)


class TestMemoize(unittest.TestCase):
    """ class for testing memoize funvtion """

    def test_memoize(self):
        """ test memoize function """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with mock.patch.object(TestClass, "a_method") as mock_a_method:
            TestClass.a_property
            TestClass.a_property
            mock_a_method.assert_called_once
