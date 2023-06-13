#!/usr/bin/python3
"""
Writing an object to a text file, using a json repr...
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj (object): python object
        filename (str): path/filename
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(json.dumbs(my_obj)))
