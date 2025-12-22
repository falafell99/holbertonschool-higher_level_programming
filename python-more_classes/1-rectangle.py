#!/usr/bin/python3
"""Rectangle class with width and height."""


class Rectangle:
    """Defines a rectangle with width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height.
        
        Args:
            width (int): Width of rectangle. Defaults to 0.
            height (int): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Get width of rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with validation.
        
        Args:
            value (int): New width value.
            
        Raises:
            TypeError: If value is not integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Get height of rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with validation.
        
        Args:
            value (int): New height value.
            
        Raises:
            TypeError: If value is not integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
