#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -3, -1, -8, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 10, 3, -8, 7]), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3,]), 3)

    def test_single_number(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_string(self):
        self.assertIsNone(max_integer(["", "", ""]))

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    def test_mixed_types(self):
        self.asserEqual(max_integer([1, "apple", 3, "banana", 2]), 3)
