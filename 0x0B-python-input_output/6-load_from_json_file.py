#!/usr/bin/python3
"""
Creating an obj from a json file
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”:

    Args:
        filename (str): json file
    """
    with open(filename, "r") as f:
        return json.load(f)
