#!/usr/bin/python3
for char in range(122, 96, -1):
    setoff = 0
    if char % 2:
        setoff = 32
    print("{:s}".format(chr(char - setoff)), end='')
