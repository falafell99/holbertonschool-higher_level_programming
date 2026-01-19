#!/usr/bin/python3
"""Student class with save/load capabilities."""


class Student:
    """Student class definition with serialization/deserialization."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: Student's first name
            last_name: Student's last name
            age: Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of Student instance with filter.

        Args:
            attrs: List of attribute names to include (optional)

        Returns:
            Dictionary representation of the Student
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from dictionary.

        Args:
            json: Dictionary with attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
