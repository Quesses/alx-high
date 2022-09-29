#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = tuple(a_dictionary.keys())
    for x in keys:
        if a_dictionary[x] == value:
            del a_dictionary[x]
    return a_dictionary
