#!/usr/bin/python3
"""Append string to file and return character count."""


def append_write(filename="", text=""):
    """Append a string to a text file and return number of characters added.

    Args:
        filename: Name of the file
        text: Text to append to the file

    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
