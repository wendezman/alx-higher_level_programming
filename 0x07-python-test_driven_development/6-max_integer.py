#!/usr/bin/python3
"""
max integer module
"""


def max_integer(list=[]):
    """
    finds the max integer from a list
    returns None if list is empty
    """
    if len(list) == 0:
        return None
    max_int = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            max_int = list[i]
        i += 1
    return max_int
