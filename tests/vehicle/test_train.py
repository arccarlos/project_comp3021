"""
Description: Unit tests for the Train class.
Author: Alex Richard Carlos
Date: September 20, 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_train.py
"""

import unittest
from vehicle.train import Train

class TestClient(unittest.TestCase):

    #setUp
    def setUp(self):
        self.train = Train("Talgo", "Avril", 12, 0.7)

    def test_init_valid(self):
        train = self.train
        self.assertEqual("Talgo", train.make)
        self.assertEqual("Avril", train.model)
        self.assertEqual(12, train._Train__cars)
        self.assertEqual(0.7, train._Train__base_fuel_rate)

    def test_make_invalid_raises(self):
        with self.assertRaises(ValueError):
            train = Train("", "Avril", 12, 0.7)
    
    def test_model_invalid_raises(self):
        with self.assertRaises(ValueError):
            train = Train("Talgo", "", 12, 0.7)
    
    def test_cars_invalid_raises(self):
        with self.assertRaises(ValueError):
            train = Train("Talgo", "Avril", "12", 0.7)
    
    def test_basefuelrate_invalid_raises(self):
        with self.assertRaises(ValueError):
            train = Train("Talgo", "Avril", 12, "0.7")
    
    def test_str_valid(self):
        train = Train("Talgo", "Avril", 12, 0.7)
        expected = "Make: Talgo\nModel: Avril\nThis train has a base fuel rate of 0.7 litres/kilometer, and contains 12 cars."
        self.assertEqual(expected, str(train))
    
    def test_fuel_requirement_valid(self):
        train = Train("Talgo", "Avril", 12, 0.7)
        distance = 500
        total_fuel = train._Train__base_fuel_rate * (1.1 * train._Train__cars)
        fuel_requirements = total_fuel * distance
        self.assertEqual(4620, round(fuel_requirements, 2))