#!/usr/bin/python3
"""BaseGeometry class with integer validator."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Calculate area - not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value.
        
        Args:
            name (str): Name of the value
            value (int): Value to validate
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
