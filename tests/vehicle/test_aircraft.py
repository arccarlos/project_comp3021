"""
Description: Unit tests for the Aircrat class.
Author: Alex Richard Carlos
Date: September 20, 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_aircraft.py
"""

import unittest
from vehicle.aircraft import Aircraft

class TestClient(unittest.TestCase):

    #setUp
    def setUp(self):
        self.aircraft = Aircraft("Boeing", "747", 42, 842)

    def test_init_valid(self):
        aircraft = self.aircraft
        self.assertEqual("Boeing", aircraft.make)
        self.assertEqual("747", aircraft.model)
        self.assertEqual(42, aircraft._Aircraft__fuel_burn_rate)
        self.assertEqual(842, aircraft._Aircraft__speed)

    def test_make_invalid_raises(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("", "747", 42, 842)
    
    def test_model_invalid_raises(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "", 42, 842)
    
    def test_fuelburnrate_invalid_raises(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "747", "42", 842)
    
    def test_speed_invalid_raises(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "747", 42, "842")
    
    def test_str_valid(self):
        aircraft = Aircraft("Boeing", "747", 42, 842)
        expected = "Make: Boeing\nModel: 747\nThis aircraft has a fuel burn rate of 42 litres/hour, and a cruising speed of 842 km/hour."
        self.assertEqual(expected, str(aircraft))
    
    def test_fuel_requirement_valid(self):
        aircraft = Aircraft("Boeing", "747", 42, 842)
        distance = 500
        flight_time = distance / aircraft._Aircraft__speed
        fuel_requirements = flight_time * aircraft._Aircraft__fuel_burn_rate
        self.assertEqual(24.94, round(fuel_requirements, 2))