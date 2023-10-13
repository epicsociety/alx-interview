#!/usr/bin/env python3
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

    if n == 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
