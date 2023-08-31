#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """
    l = len(list_of_integers)
    if l < 4:
        if l == 1:
            return list_of_intergers[0]
        if l <= 1:
            return
        return max(list_of_integers)
    else:
        return find_peak([list_of_integers[0], find_peak(list_of_integers[1:-1]), list_of_integers[-1]])
