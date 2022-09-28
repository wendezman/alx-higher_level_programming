#!/usr/bin/python3
"""
The function 6-load_from_json_file.py
"""

import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as myfile:
        object_created = json.load(myfile)
        return object_created
