#!/usr/bin/python3
"""
Writing a string to a .txt file
"""


def write_file(filename="", text=""):
    """
    This Function writes a string to a text file
    (UTF8) and returns the number of characters written:
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
            return len(text)
    except TypeError:
        return 0
