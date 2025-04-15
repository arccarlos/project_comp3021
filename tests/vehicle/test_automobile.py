"""
Description: Unit tests for the Automobile class.
Author: Alex Richard Carlos
Date: September 20, 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_automobile.py
"""

import unittest
from vehicle.automobile import Automobile

class TestClient(unittest.TestCase):

    #setUp
    def setUp(self):
        self.automobile = Automobile("Honda", "Civic", 7)
        
    def test_init_valid(self):
        automobile = self.automobile
        self.assertEqual("Honda", automobile.make)
        self.assertEqual("Civic", automobile.model)
        self.assertEqual(7, automobile._Automobile__kilometers_per_litre)
    
    def test_make_invalid_raises(self):
        with self.assertRaises(ValueError):
            automobile = Automobile("", "Civic", 7)

    def test_model_invalid_raises(self):
        with self.assertRaises(ValueError):
            automobile = Automobile("Honda", "", 7)

    def test_kmpl_invalid_raises(self):
        with self.assertRaises(ValueError):
            automobile = Automobile("Honda", "Civic", "7")

    def test_str_valid(self):
        automobile = Automobile("Honda", "Civic", 7)
        expected = "Make: Honda\nModel: Civic\nThis automobile can drive 7 kilometers per litre."
        self.assertEqual(expected, str(automobile))

    def test_fuel_requirement_valid(self):
        automobile = Automobile("Honda", "Civic", 7)
        fuel_requirements = (500 / automobile._Automobile__kilometers_per_litre)
        self.assertEqual(71.43, round(fuel_requirements, 2))