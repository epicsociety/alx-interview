#!/usr/bin/python3
"""
Module contains interview question on
minimum number of operationss to reach n characters
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    Args(int): n
    Return(int): total number of operations
    """

    if n < 2:
        return 0

    operations, characters = 0, 2
    # a loop that continues as long as charaters are <= n
    while characters <= n:
        # checks if n is divisible evenly by characters
        if n % characters == 0:
            # If factor of n, adds characters to the operations
            operations = characters + operations
            # Update n to be the result of dividing n by characters
            n = n / characters
            # Reduces characters by 1 to find other smaller factors
            characters -= 1
        # increments characterss by 1 for the next iteration of the loop
        characters += 1
    return operations
