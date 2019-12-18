#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        [print("{:d}".format(integer)) for integer in my_list[::-1]]
