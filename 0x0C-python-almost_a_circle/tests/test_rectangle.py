#!/usr/bin/python3
"""
"""
import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """
    """
    def test_general(self):
        """
        """
        #Arrange
        w = 10
        h = 2
        r1 = Rectangle(w, h)
        r2 = Rectangle(12, 22, 3, 3, 12)

        #Act
        id1 = r1.id 
        w1 = r1.width
        h1 = r1.height
        x1 = r1.x
        y1 = r1.y

        id2 = r2.id
        w2 = r2.width
        h2 = r2.height
        x2 = r2.x
        y2 = r2.y
        
        #Assert
        self.assertEqual(id1, 1)
        self.assertEqual(w1, w)
        self.assertEqual(h1, h)
        self.assertEqual(x1, 0)
        self.assertEqual(y1, 0)

        self.assertEqual(id2, 12)
        self.assertEqual(w2, 12)
        self.assertEqual(h2, 22)
        self.assertEqual(x2, 3)
        self.assertEqual(y2, 3)

if __name__ == "__main__":
    unittest.main()
