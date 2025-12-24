#!/usr/bin/python3
"""MyList class that inherits from list."""


class MyList(list):
    """Custom list class with additional methods."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
