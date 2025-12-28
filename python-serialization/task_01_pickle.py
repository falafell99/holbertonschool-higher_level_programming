#!/usr/bin/python3
"""Pickling custom classes module."""

import pickle


class CustomObject:
    """Custom class for pickling demonstration."""

    def __init__(self, name, age, is_student):
        """
        Initialize CustomObject instance.

        Args:
            name (str): Name of the person
            age (int): Age of the person
            is_student (bool): Student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display object attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Args:
            filename (str): Name of the file to save the object to

        Returns:
            None on error, otherwise nothing
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Args:
            filename (str): Name of the file to load the object from

        Returns:
            CustomObject instance or None on error
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
