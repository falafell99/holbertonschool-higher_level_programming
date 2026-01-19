#!/usr/bin/python3
"""Student class with JSON serialization."""


class Student:
    """Student class definition."""

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

    def to_json(self):
        """Retrieve dictionary representation of Student instance.

        Returns:
            Dictionary representation of the Student
        """
        return self.__dict__
