#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    for n in matrix:
        for i in range(len(n)):
            print("{:d}".format(n[i]), end="")
            if i != len(n) - 1:
                print(" ", end="")

        print("")


"""
def print_matrix_integerr(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            if j != len(row) - 1:
                ender = " "
            else:
                ender = ""
            print("{:d}".format(row[j]), end= ender)
        print("")
"""
