#!/usr/bin/python3
"""
python object to json
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string):
    Args:
        my_obj (object): object
    """
    return (json.dumps(my_obj))
