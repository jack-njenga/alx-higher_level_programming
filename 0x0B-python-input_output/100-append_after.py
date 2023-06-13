#!/usr/bin/python3
"""
Appending data after certain charcters
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file,
    after each line containing a specific string 

    Args:
        filename (str): filename
        search_string (str): string to seach for
        new_string (str): string to add
    """
    my_list = []
    with open(filename, "r", encoding="utf-8") as f:
        my_list = f.readlines()
        i = 0
        while i < len(my_list):
            if search_string in my_list[i]:
                my_list[i:(i + 1)] = [my_list[i], new_string]
                i += 1
            i += 1
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(my_list)
