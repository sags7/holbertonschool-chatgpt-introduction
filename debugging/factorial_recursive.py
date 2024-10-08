#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given integer. Returns 1 if the input is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
