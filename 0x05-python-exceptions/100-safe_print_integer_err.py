#!/usr/bin/python3
import traceback as tb
def safe_print_integer_err(value):
from sys import stderr
    try:
        print("{:d}".format(value))
        return True
