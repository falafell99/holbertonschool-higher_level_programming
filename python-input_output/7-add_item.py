#!/usr/bin/python3
"""Add all arguments to a list and save to JSON file."""

import sys
import os


# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Main function to add arguments to list and save to file."""
    filename = "add_item.json"

    # Load existing list or create empty list if file doesn't exist
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to file
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
