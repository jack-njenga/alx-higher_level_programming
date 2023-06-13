#!/usr/bin/python3
"""
This functon reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    reads a text file and print it to the stdout.

    Args:
        filename (str): the filename
    """
    with open(filename, "r", encoding="utf8") as f:
        data = f.read()

    print(data, end="")
