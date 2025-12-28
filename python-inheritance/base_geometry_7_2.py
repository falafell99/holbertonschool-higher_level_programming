#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Method that raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value:
        - name is always a string
        - value must be an integer (not a boolean or float)
        - value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
