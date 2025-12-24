#!/usr/bin/python3
"""Function to check if object is instance of or inherits from class."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance of or inherits from specified class.
    
    Args:
        obj: Object to check.
        a_class: Class to compare against.
        
    Returns:
        bool: True if obj is instance of a_class or inherited from it.
    """
    return isinstance(obj, a_class)
