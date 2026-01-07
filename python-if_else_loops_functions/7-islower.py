#!/usr/bin/python3
def islower(c):
    """Check if character is lowercase."""
    if len(c) == 0:
        return False
    ascii_val = ord(c)
    return 97 <= ascii_val <= 122
