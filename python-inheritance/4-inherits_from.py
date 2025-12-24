#!/usr/bin/python3
"""Function to check if object inherits from class."""


def inherits_from(obj, a_class):
    """Check if object inherits from specified class.
    
    Args:
        obj: Object to check.
        a_class: Class to compare against.
        
    Returns:
        bool: True if obj inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
