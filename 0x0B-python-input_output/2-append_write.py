#!/usr/bin/python3
"""
Appending a string
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added:
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(text)
            return len(text)
    except TypeError:
        pass
