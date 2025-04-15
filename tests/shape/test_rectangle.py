"""
Description: Unit tests for the Rectangle class.
Author: Alex Richard Carlos
Date: September 19, 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_rectangle.py
"""

import unittest

from shape.rectangle import Rectangle

class TestClient(unittest.TestCase):

    #setup
    def setUp(self):
        self.rectangle = Rectangle("black", 4, 10)

    def test_init_valid_rectangle(self):
        rectangle = self.rectangle
        self.assertEqual("black", rectangle._color)
        self.assertEqual(4, rectangle._Rectangle__length)
        self.assertEqual(10, rectangle._Rectangle__width)

    def test_color_invalid_raises(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("", 4, 10)

    def test_length_invalid_raises(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("black", "4", 10)
    
    def test_width_invalid_raises(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("black", 4, "10")
    
    def test_str_valid(self):
        rectangle = Rectangle("black", 4, 10)
        expected = "The shape color is black.\nThis rectangle has four sides with the lengths of 4, 10, 4 and 10 centimeters."
        self.assertEqual(expected, str(rectangle))
    
    def test_calculate_area_valid(self):
        rectangle = Rectangle("black", 4, 10)
        area = rectangle._Rectangle__length * rectangle._Rectangle__width
        self.assertEqual(rectangle.calculate_area(), area)

    def test_calculate_perimeter_valid(self):
        rectangle = Rectangle("black", 4, 10)
        perimeter = rectangle._Rectangle__length * 2 + rectangle._Rectangle__width * 2
        self.assertEqual(rectangle.calculate_perimeter(), perimeter)