"""
Description: Unit tests for the Book class.
Author: Alex Richard Carlos
Date: September 19, 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_triangle.py
"""

import unittest
import math
from shape.triangle import Triangle

class TestClient(unittest.TestCase):

    # SetUp
    def setUp(self):
        self.triangle = Triangle("black", 3, 4, 5)

    def test_init_valid(self):
        triangle = self.triangle
        self.assertEqual("black", triangle._color)
        self.assertEqual(3, triangle._Triangle__side_1)
        self.assertEqual(4, triangle._Triangle__side_2)
        self.assertEqual(5, triangle._Triangle__side_3)
    
    def test_color_invalid_raises(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("", 3, 4, 5)

    def test_side1_invalid_raises(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("black", "3", 4, 5)

    def test_side2_invalid_raises(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("black", 3, "4", 5)
    
    def test_side3_invalid_raises(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("black", 3, 4, "5")
    
    def test_str_valid(self):
        triangle = Triangle("black", 3, 4, 5)
        expected = "The shape color is black.\nThis triangle has three sides with the lengths 3, 4, 5."
        self.assertEqual(str(triangle), expected)
    
    def test_calculate_area_valid(self):
        triangle = Triangle("black", 3, 4, 5)
        semi_perimeter = (triangle._Triangle__side_1 + triangle._Triangle__side_2 + triangle._Triangle__side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - triangle._Triangle__side_1) * (semi_perimeter - triangle._Triangle__side_2) * (semi_perimeter - triangle._Triangle__side_3))
        self.assertEqual(triangle.calculate_area(), area)

    def test_calculate_perimeter_valid(self):
        triangle = Triangle("black", 3, 4, 5)
        perimeter = triangle._Triangle__side_1 + 4 + triangle._Triangle__side_3
        self.assertEqual(triangle.calculate_perimeter(), perimeter)

