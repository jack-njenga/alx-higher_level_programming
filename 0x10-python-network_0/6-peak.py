#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """
    ln = len(list_of_integers)
    if ln < 4:
        if ln == 1:
            return list_of_intergers[0]
        if ln < 2:
            return
        return max(list_of_integers)
    else:
        return find_peak([list_of_integers[0],
                         find_peak(list_of_integers[1:]),
                         list_of_integers[-1]])
