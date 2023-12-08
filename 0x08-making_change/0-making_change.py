#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    return num_coins if total == 0 else -1


# DEEMED INEFFICIENT FOR LARGE NUMBER OF COINS
# def makeChange(coins, total):
#     if total <= 0:
#         return 0

#     # Initialize dp array with a large value
#     dp = [float('inf')] * (total + 1)
#     dp[0] = 0

#     # Iterate through each coin value
#     for coin in coins:
#         # Update dp array for each possible total
#         for i in range(coin, total + 1):
#             dp[i] = min(dp[i], dp[i - coin] + 1)

#     # Check if the total can be achieved
#     if dp[total] == float('inf'):
#         return -1
#     else:
#         return dp[total]
