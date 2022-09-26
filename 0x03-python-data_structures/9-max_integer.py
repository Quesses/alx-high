#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        length = len(my_list) - 1
        while length > 1:
            index = 0
            while index < length:
                if my_list[index] < my_list[index + 1]:
                    temp = my_list[index]
                    my_list[index] = my_list[index + 1]
                    my_list[index + 1] = temp
            y += 1
        x -= 1
    return my_list[0]
