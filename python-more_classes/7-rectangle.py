#!/usr/bin/python3
"""Rectangle class with customizable print symbol."""


class Rectangle:
    """Defines a rectangle with width and height."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height.
        Args:
            width (int): Width of rectangle. Defaults to 0.
            height (int): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculate and return the area of the rectangle.
        Returns:
            int: Area of rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.
        Returns:
            int: Perimeter of rectangle (2 * (width + height)).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle with print_symbol.
        Returns:
            str: Rectangle represented with print_symbol.
            Returns empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        rect_str = ""
        for i in range(self.__height):
            rect_str += symbol * self.__width
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Return official string representation of rectangle.
        Returns:
            str: String that can be used with eval() to create a new instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when rectangle is deleted and decrement counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
