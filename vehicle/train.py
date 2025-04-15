""""
Description: A class to represent Train objects.
Author: Alex Richard Carlos
Date: September 19, 2024
"""

from vehicle.vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, make: str, model: str, cars: int, base_fuel_rate: float):
        super().__init__(make, model)
        """
            Initializes an Train based on received args (if valid).

            Args:
                make(str): the make of the train.
                model(str): the model of the train.
                cars(int): the cars on the train.
                base_fuel_rate(float): the base fuel rate of the train.

            Raises:
                ValueError: if any of the arguments is invalid.
        """
        if not isinstance(cars, (int)):
            raise ValueError("Cars must be numeric.")
        else:
            self.__cars = cars

        if not isinstance(base_fuel_rate, (int, float)):
            raise ValueError("Fuel burn rate must be numeric.")
        else:
            self.__base_fuel_rate = base_fuel_rate

    def __str__(self) -> str:
        """
            Returns: str - returns a string using the attributes of the train class.

            Example:
                Make: Talgo
                Model: Avril
                This train has a base fuel rate of 0.7 litres/kilometer, and contains 12 cars.
        """
        return super().__str__() + f"\nThis train has a base fuel rate of {self.__base_fuel_rate} litres/kilometer, and contains {self.__cars} cars."
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
            Calculates the fuel requirement of the train given its distance.

            Return: float - the fuel requirement.
        """
        total_fuel = self.__base_fuel_rate * (1.1 * self.__cars)
        fuel_requirements = total_fuel * distance
        return fuel_requirements