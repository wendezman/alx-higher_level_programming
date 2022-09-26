#!/usr/bin/python3
"""
The function 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    check if the object is exactly an instance of the specified class
    Args:
        obj: initial object
        a_class: class to confirm
        Returns: True if object is an exactly the instance of
        the class or False otherwise
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
