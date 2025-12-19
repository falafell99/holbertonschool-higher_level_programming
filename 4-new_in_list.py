#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position
    without modifying the original list."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy
    new_list = my_list[:]  # Create a copy of the list
    new_list[idx] = element  # Modify element in the copy
    return new_list
