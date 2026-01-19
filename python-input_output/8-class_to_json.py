#!/usr/bin/python3
"""Convert class instance to JSON-serializable dictionary."""


def class_to_json(obj):
    """Return dictionary description for JSON serialization of an object.

    Args:
        obj: Instance of a class

    Returns:
        Dictionary with serializable attributes
    """
    return obj.__dict__
