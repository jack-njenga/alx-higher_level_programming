#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = [row[:] for row in matrix]
    for lt in new:
        for n in range(len(lt)):
            lt[n] = lt[n] ** 2

    return (new)
