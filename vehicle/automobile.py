""""
Description: A class to represent Automobile objects.
Author: Alex Richard Carlos
Date: September 19, 2024
"""

from vehicle.vehicle import Vehicle

class Automobile(Vehicle):
    def __init__(self, make: str, model: str, kilometers_per_litre: float):
        super().__init__(make, model)
        """
            Initializes an Automobile based on received args (if valid).

            Args:
                make(str): the make of the automobile.
                model(str): the model of the automobile.
                kilometers_per_litre(float): the kilometers per litre of the automobile.

            Raises:
                ValueError: if any of the arguments is invalid.
        """

        if not isinstance(kilometers_per_litre, (int, float)):
            raise ValueError("Kilometers per litre must be numeric.")
        else:
            self.__kilometers_per_litre = kilometers_per_litre

    def __str__(self) -> str:
        """
            Returns: str - returns a string using the attributes of the automobile class.

            Example:
                Make: Honda
                Model: Civic
                This automobile can drive 12 kilometers per litre.
        """
        return super().__str__() + f"\nThis automobile can drive {self.__kilometers_per_litre} kilometers per litre."
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
            Calculates the fuel requirement of the automoboile given its distance.

            Return: float - the fuel requirement.
        """
        fuel_requirements = distance / self.__kilometers_per_litre
        return fuel_requirements