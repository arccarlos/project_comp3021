""""
Description: A class to represent generic Vehicle objects.
Author: Alex Richard Carlos
Date: September 19, 2024
"""
from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, make: str, model: str):
        """
            Initializes a Vehicle based on received args (if valid).

            Args:
                make(str): the make of the vehicle.
                model(str): the model of the vehicle.

            Raises:
                ValueError: if any of the arguments is invalid.
        """

        if not len(make.strip()):
            raise ValueError("Make cannot be blank.")
        else:
            self.__make = make

        if not len(model.strip()) > 0:
            raise ValueError("Model cannot be blank.")
        else:
            self.__model = model

    @property
    def make(self) -> str:
        """
        Accessor for the make attribute.
        Returns: str - the make of the Vehicle instance.
        """
        return self.__make
    
    @property
    def model(self) -> str:
        """
        Accessor for the model attribute.
        Returns: str - the model of the Vehicle instance.
        """
        return self.__model
    
    def __str__(self) -> str:
        """
            Returns: str - returns a string using the attributes of the Vehicle class.

            Example:
                Make: Honda
                Model: Civic
        """
        return f"Make: {self.__make}\nModel: {self.__model}"
    
    @abstractmethod
    def calculate_fuel_requirements(self, distance: float) -> float:
        pass