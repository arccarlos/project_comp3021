""""
Description: A class to represent Triangle objects.
Author: Alex Richard Carlos
Date: September 19, 2024
"""

import math
from shape.shape import Shape

class Triangle(Shape):
    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        super().__init__(color)
        """
            Initializes a Triangle based on received args (if valid).

            Args:
                color(str): the color of the shape.
                side_1(int): the 1st side of the triangle.
                side_2(int): the 2nd side of the triangle.
                side_3(int): the 3rd side of the triangle.

            Raises:
                ValueError: if any of the arguments is invalid.
        """

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")
        else:
            self.__side_1 = side_1

        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        else:
            self.__side_2 = side_2

        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")
        else:
            self.__side_3 = side_3
        
    def __str__(self) -> str:
        """
            Returns: str - returns a string using the attributes of the Triangle class.

            Example:
                The shape color is red.
                This triangle has three sides with the lengths 3, 4, 5.
        """
        return super().__str__() + f"\nThis triangle has three sides with the lengths {self.__side_1}, {self.__side_2}, {self.__side_3}."

    def calculate_area(self) -> float:
        """
            Calculates the area of the triangle given its sides.

            Returns: float - the area of the triangle.
        """
        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.__side_1) * (semi_perimeter - self.__side_2) * (semi_perimeter - self.__side_3))
        return area
    
    def calculate_perimeter(self) -> float:
        """
            Calculates the area of the triangle given its sides.

            Return: float - the perimeter of the triangle.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        return perimeter