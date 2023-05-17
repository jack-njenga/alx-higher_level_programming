#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = [row[:] for row in matrix]
    for l in new:
        for n in range(len(l)):
            l[n] = l[n] ** 2

    return (new)
