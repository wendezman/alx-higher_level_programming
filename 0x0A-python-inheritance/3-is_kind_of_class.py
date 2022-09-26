#!/usr/bin/python3
"""
The function 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instance of a specified class
    Args:
        obj: initial object
        a_class: class to confirm
        Returns: True if object is an instance of
        the class or False otherwise
    """
    return isinstance(obj, a_class)
