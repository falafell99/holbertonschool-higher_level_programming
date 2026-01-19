#!/usr/bin/python3
"""Write string to file and return character count."""


def write_file(filename="", text=""):
    """Write a string to a text file and return number of characters.

    Args:
        filename: Name of the file to write
        text: Text to write to the file

    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
