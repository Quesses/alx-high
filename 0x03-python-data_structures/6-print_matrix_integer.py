#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x in row:
            print("{}".format(x), end=" ")
        print("")
