#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize a variable to count the number of coins
    num_coins = 0

    # Iterate through each coin
    for coin in coins:
        # While the current coin can be used to reduce the total
        while total >= coin:
            # Reduce the total by the value of the current coin
            total -= coin
            # Increment the coin count
            num_coins += 1

    # If the total is reduced to 0, return the number of coins
    # Otherwise, it means the total cannot be achieved with the given coins
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
