#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""

        try:
            for attribute in attrs:
                if not isinstance(attribute, str):
                    return self.__dict__
        except Exception:
            return self.__dict__

        my_dict = dict()
        for key, val in self.__dict__.items():
            if key in attrs:
                my_dict[key] = val
        return my_dict
