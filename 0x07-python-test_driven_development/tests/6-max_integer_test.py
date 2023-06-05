#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unittest class

    Args:
        unittest.TestCase (TestMaxInteger):

    """
    def test_empty(self):
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-21, -271, -98, -198]), -21)
        self.assertEqual(max_integer([2, 4, 6, 6]), 6)
        self.assertEqual(max_integer([False, True]), 1)
        self.assertEqual(max_integer([0]), False)
