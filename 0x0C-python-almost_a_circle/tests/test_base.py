#!/usr/bin/python3
"""
Testing module for Base class
"""
import unittest
from models.base import Base



class Base_test(unittest.TestCase):
    """
    Base_test - Tests the Base class
    """
    def test_1(self):
        """
        This is a basic normal test
        """
        #Arrange
        ids = 100

        #Act
        b1 = Base()
        id_1 = b1.id

        b2 = Base()
        id_2 = b2.id

        b3 = Base(ids)
        id_3 = b3.id

        #Assert
        self.assertEqual(id_1, 1)
        self.assertEqual(id_2, 2)
        self.assertEqual(id_3, ids)
