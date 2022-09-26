#!/usr/bin/python3
"""
The function 11-square.py
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size):
        """Initializing the function
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns the area"""
        return super().area()

    def __str__(self):
        """returns square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
