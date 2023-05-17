#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda _list: list(map(lambda num: num ** 2, _list)), (matrix))))
