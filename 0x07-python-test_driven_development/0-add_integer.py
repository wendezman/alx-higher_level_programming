#!/usr/bin/python3
""" add integer module """


def add_integer(a, b=98):
    """
    adds 2 integers
    Args:
        a: first integer
        b: second integer
    Returns:
        the sum of 2 integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        second_a, second_b = int(a), int(b)
        return second_a + second_b
