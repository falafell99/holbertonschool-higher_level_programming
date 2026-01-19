#!/usr/bin/python3
"""Load object from JSON file."""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename: Name of the JSON file to read

    Returns:
        Python object loaded from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
