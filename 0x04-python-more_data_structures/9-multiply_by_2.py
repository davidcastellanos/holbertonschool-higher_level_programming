#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary is not None:
        for k in a_dictionary.keys():
            new_dict[k] = a_dictionary[k] * 2
    return new_dict
