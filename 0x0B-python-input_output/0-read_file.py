#!/usr/bin/python3
"""
The function 0-read_file.py
"""


def read_file(filename=""):
    """reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as myfile:
        readfile = myfile.read()
        print(readfile, end="")
