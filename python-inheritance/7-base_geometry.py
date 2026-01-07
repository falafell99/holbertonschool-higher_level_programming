#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with public instance methods
"""


class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """
        Public instance method that raises an Exception
        with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value:
        - name is always a string
        - value must be an integer, otherwise raise TypeError
        - value must be greater than 0, otherwise raise ValueError
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
