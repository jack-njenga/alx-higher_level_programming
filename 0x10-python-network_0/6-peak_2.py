#!/usr/bin/python3
"""
...
"""
def find_peak(list_of_integers, index=0):
    """
    ...
    """
    if index == len(list_of_integers) - 1:
        return list_of_integers[index]

    max_number = find_peak(list_of_integers, index + 1)
    if list_of_integers[index] > max_number:
        max_number = list_of_integers[index]
    return max_number
