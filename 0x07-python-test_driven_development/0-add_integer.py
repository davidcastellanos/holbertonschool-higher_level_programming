#!/usr/bin/python3
"""Function that adds 2 integers.
    $ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
"""


def add_integer(a, b):
    """Add two integers
    Args:
        a: First integer to add. If type(a) is float, it is first
            casted to an int.
        b: Second integer to add. If type(b) is float, it is first
            casted to an int.

    Returns:
        Sum of `a` and `b`

    Raises:
        TypeError: If `type(a)` or `type(b)` is neither an int nor
        float.
"""
    if a != a or not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if b != b or not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    res = a + b
    if abs(res) == float('inf'):
        raise OverflowError('overflow error')
    return int(a) + int(b)
