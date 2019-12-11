#!/usr/bin/python3
def uppercase(str):
    for char in str:
        setoffs = 0
        if ord(char) > 96 and ord(char) < 123:
            setoffs = -32
        print("{:s}".format(chr(ord(char) + setoffs)), end='')
    else:
        print()
