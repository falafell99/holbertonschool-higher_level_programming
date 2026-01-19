#!/usr/bin/python3
"""Convert JSON string to object."""

import json


def from_json_string(my_str):
    """Return object represented by a JSON string.

    Args:
        my_str: JSON string to deserialize

    Returns:
        Python object represented by the JSON string
    """
    return json.loads(my_str)
