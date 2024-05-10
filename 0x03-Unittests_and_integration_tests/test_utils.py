#!/usr/bin/env python3
''' utils tests '''
import unittest
from parameterized import parameterized, param
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    ''' test cases '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' test '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        ''' tests exception '''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected)


class TestGetJson(unittest.TestCase):
    ''' test get json '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        ''' test json response '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            result = get_json(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    ''' test memoize '''
    def test_memoize(self):
        class TestClass:
            ''' test class '''

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        my_ins = TestClass()
        with patch.object(my_ins, 'a_method', return_value=42) as mocked:
            result = my_ins.a_property()
            result1 = my_ins.a_property()
            mocked.assert_called_once()
            self.assertEqual(result, 42)
