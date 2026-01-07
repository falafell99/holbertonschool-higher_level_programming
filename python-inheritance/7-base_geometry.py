#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
It includes methods for area calculation and integer validation.
"""


class BaseGeometry:
    """
    BaseGeometry class with public instance methods area and integer_validator.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        Message: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a strictly positive integer.

        Args:
            name (str): The name of the value (assumed string).
            value (int): The value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
