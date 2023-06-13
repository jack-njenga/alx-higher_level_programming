#!/usr/bin/python3
"""
json string to python object
"""


def from_json_string(my_str):
    import json
    """
    returns an object (Python data structure) represented
    by a JSON stringi.
    
    Args:
        my_str (str): a jason string
    """
    return (json.loads(my_str))
