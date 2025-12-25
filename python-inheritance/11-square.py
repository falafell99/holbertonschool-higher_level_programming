#!/usr/bin/python3
"""Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with size.
        Args:
            size (int): Size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation of square.
        Returns:
            str: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
