#!/usr/bin/python3
"""
The function 100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string
    """
    inserted = []
    with open(filename, "r", encoding="utf-8") as myfile:
        inserted = myfile.readlines()
        index = 0
        while index < len(inserted):
            if search_string in inserted[index]:
                inserted[index:index + 1] = [inserted[index], new_string]
                index += 1
            index += 1
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.writelines(inserted)
