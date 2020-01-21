#!/usr/bin/python3
"""Module with function that returns True if the object is an instance 
of a class that inherited (directly or indirectly) 
from the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """Checks if obj is inherits from a_class
    Args:
        obj - object to be checked
        a_class - class to compare against
    Return:
        bool - True if obj is an instance of a_class, False otherwise
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
