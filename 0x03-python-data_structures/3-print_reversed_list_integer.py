#!/bin/usr/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    last = len(my_list) - 1
    while last >= 0:
        print("{:d}".format(my_list[last]))
        last -= 1
