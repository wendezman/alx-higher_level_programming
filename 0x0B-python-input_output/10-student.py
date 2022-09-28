#!/usr/bin/python3
"""
The class student
"""


class Student:
    """defines a student by:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        retrieves a dictionary representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """retrieves a dictionary representation of a Student instance"""
        if attr is not None:
            result = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return result
        else:
            return self.__dict__
