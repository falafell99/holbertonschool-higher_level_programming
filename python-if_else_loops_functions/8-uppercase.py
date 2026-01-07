#!/usr/bin/python3
def uppercase(str):
    """Print string in uppercase."""
    result = ""
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:  # lowercase
            result += chr(ascii_val - 32)
        else:
            result += char
    print("{}".format(result))
