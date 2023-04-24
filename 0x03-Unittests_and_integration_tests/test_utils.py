#!/usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make
sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for 
ollowing inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
	"""_summary_

	Args:
					unittest (_type_): _description_
	"""

	@parameterized.expand(
		[
			({"a": 1}, ("a",), 1),
			({"a": {"b": 2}}, ("a",), {"b": 2}),
			({"a": {"b": 2}}, ("a", "b"), 2)
		]
	)
	def test_access_nested_map(self, nested_map, path, expected_output):
		"""_summary_
		"""
		result = access_nested_map(nested_map, path)
		self.assertEqual(result, expected_output)

	@parameterized.expand(
		[
			({}, ("a",), KeyError),
			({"a": 1}, ("a", "b"), KeyError)
		]
	)
	def test_access_nested_map_exception(self, nested_map, path, expected_output):
		"""_summary_
		"""
		with self.assertRaises(expected_output) as context:
			access_nested_map(nested_map, path)
