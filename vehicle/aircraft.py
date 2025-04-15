""""
Description: A class to represent Aircraft objects.
Author: Alex Richard Carlos
Date: September 19, 2024
"""

from vehicle.vehicle import Vehicle

class Aircraft(Vehicle):
    def __init__(self, make: str, model: str, fuel_burn_rate: float, speed: float):
        super().__init__(make, model)
        """
            Initializes an Aircraft based on received args (if valid).

            Args:
                make(str): the make of the aircraft.
                model(str): the model of the aircraft.
                fuel_burn_rate(float): the fuel burn rate of the aircraft.
                speed(float): the speed of the aisrcraft.

            Raises:
                ValueError: if any of the arguments is invalid.
        """
        if not isinstance(fuel_burn_rate, (int, float)):
            raise ValueError("Fuel burn rate must be numeric.")
        else:
            self.__fuel_burn_rate = fuel_burn_rate

        if not isinstance(speed, (int, float)):
            raise ValueError("Speed must be numeric.")
        else:
            self.__speed = speed

    def __str__(self) -> str:
        """
            Returns: str - returns a string using the attributes of the aircraft class.

            Example:
                Make: Boeing
                Model: 747
                This aircraft has a fuel burn rate of 42 litres/hour, and a cruising speed of 842 km/hour.
        """
        return super().__str__() + f"\nThis aircraft has a fuel burn rate of {self.__fuel_burn_rate} litres/hour, and a cruising speed of {self.__speed} km/hour."
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
            Calculates the fuel requirement of the aircraft given its distance.

            Return: float - the fuel requirement.
        """
        flight_time = distance / self.__speed
        fuel_requirements = flight_time * self.__fuel_burn_rate
        return fuel_requirements