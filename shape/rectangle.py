""""
Description: A class to represent Rectangle objects.
Author: Alex Richard Carlos
Date: September 19, 2024
"""

from shape.shape import Shape

class Rectangle(Shape):
    def __init__(self, color: str, length: int, width: int):
        super().__init__(color)
        """
            Initializes a Triangle based on received args (if valid).

            Args:
                color(str): the color of the shape.
                length(int): the length of the rectangle.
                width(int): the width of the rectangle.

            Raises:
                ValueError: if any of the arguments is invalid.
        """

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        else:
            self.__length = length

        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")
        else:
            self.__width = width
        
    def __str__(self) -> str:
        """
            Returns: str - returns a string using the attributes of the Triangle class.

            Example:
                The shape color is red.
                This rectangle has four sides with the lengths of 4, 10, 4 and 10 centimeters.
        """
        return super().__str__() + f"\nThis rectangle has four sides with the lengths of {self.__length}, {self.__width}, {self.__length} and {self.__width} centimeters."
    
    def calculate_area(self) -> float:
        """
            Calculates the area of the triangle given its sides.

            Returns: float - the area of the rectangle.
        """
        area = self.__length * self.__width
        return area
    
    def calculate_perimeter(self) -> float:
        """
            Calculates the area of the triangle given its sides.

            Returns: float - the perimeter of the rectangle.
        """
        perimeter = self.__length * 2 + self.__width * 2
        return perimeter