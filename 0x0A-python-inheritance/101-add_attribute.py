#!/usr/bin/python3
"""
The function 101-add_attribute.py
"""


def add_attribute(obj, objname, value):
    """adds a new attribute to an object
    Args:
        obj: class object
        objname: object name
        value: value of attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
