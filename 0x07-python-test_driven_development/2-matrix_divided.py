#!/bin/python3
"""
This function divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """
    divides all elements of the matrix with div.
    Args:
        matrix (list of lists): this is a list of lists
        div (int): must be a number (integer or float)
    Return:
        a new matrix (list of lists)

    #doctest
    >>> matrix = [[1, 2, 3],[4, 5, 6]]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided([[]], 0))
    Traceback (most recent call last):
      File "./2-main.py", line 11, in <module>
        print(matrix_divided([[]], 0))
      File "/mnt/c/GIT/ME/alx-higher_level_programming/0x07-python-test_driven_development/2-matrix_divided.py", line 40, in matrix_divided
        raise ZeroDivisionError("division by zero")
    ZeroDivisionError: division by zero
    
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
        raise TypeError(err)
    if len(matrix) == 0:
        raise TypeError(err)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(err)
        else:
            for num in row:
                if not isinstance(num, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    ans = []
    for row in matrix:
        _row = []
        for num in row:
            _row.append(round((num / div), 2))
        ans.append(_row)

    return ans
