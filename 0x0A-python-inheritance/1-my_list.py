#!/usr/bin/python3
"""Module that prints the list, but sorted (ascending sort)"""

class MyList(list):
    """Custom List Type Class"""

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
