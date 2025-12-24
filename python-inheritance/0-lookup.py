#!/usr/bin/python3
"""Function to return attributes and methods of an object."""


def lookup(obj):
    """Return list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object.
        
    Returns:
        list: Sorted list of attributes and methods.
    """
    return dir(obj)
