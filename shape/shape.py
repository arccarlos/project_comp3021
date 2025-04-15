""""
Description: A class to represent generic Shape objects.
Author: ALex Richard Carlos
Date: September 19, 2024
"""

from abc import ABC, abstractmethod

class Shape:
    """
    Shape Class. Represents shapes.
    """
    def __init__(self, color: str):
        """
            Initializes a Shape based on received args (if valid).

            Args:
                color(str): the color of the shape.

            Raises:
                ValueError: if any of the argumanets is invalid.
        """
        if not len(color.strip()) > 0:
            raise ValueError("Color cannot be blank.")
        else:
            self._color = color

    def __str__(self) -> str:
        """
            Returns: str - returns a string using the attributes of the Shape class.

            Example:
                The shape color is red.
        """
        return f"The shape color is {self._color}."
    
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass