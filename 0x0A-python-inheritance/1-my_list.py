#!/usr/bin/python3
"""
MyList class inherit from list
"""


class MyList(list):
    """MyList class that inherits from list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
