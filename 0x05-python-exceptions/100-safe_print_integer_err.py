#!/usr/bin/python3
import traceback as tb
def safe_print_integer_err(value):
ret = False
    try:
        print("{:d}".format(value))
        ret = True
