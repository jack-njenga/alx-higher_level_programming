#!/usr/bin/python3

"""
This function prints a text and 2 "\n" after any of these characters: (. ? :)
"""


def text_indentation(text):
    """
    prints a text and 2 "\n" after any of these characters: (. ? :)

    Args:
        text (str): text to print print

    Doctests:
    >>> text_indentation("Hello. world? nice: to meet you")
    Hello.
    <BLANKLINE>
     world?
    <BLANKLINE>
     nice:
    <BLANKLINE>
     to meet you
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = [".", "?", ":"]
    i = 0
    for c in text:
        print(c, end="")
        if c in chars:
            print("\n" * 2, end="")
