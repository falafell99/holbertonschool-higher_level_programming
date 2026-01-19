#!/usr/bin/python3
"""Convert object to JSON string."""

import json


def to_json_string(my_obj):
    """Return JSON representation of an object.

    Args:
        my_obj: Object to serialize to JSON

    Returns:
        JSON string representation of the object
    """
    return json.dumps(my_obj)
