#!/usr/bin/python3
"""
Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    # Create array to store the minimum number of coins needed for each value
    MinCoins = [float('inf')] * (total + 1)
    # The minimum number of coins needed for 0 is 0
    MinCoins[0] = 0
    # Loop through each value from 1 to the desired total
    for i in range(1, total + 1):
        # Loop through each coin in the coins list
        for coin in coins:
            # If the coin is less than or equal to the current value
            if coin <= i:
                # Update the minimum number of coins needed for this value
                MinCoins[i] = min(MinCoins[i], 1 + MinCoins[i - coin])
    # If the minimum number of coins is still infinity, it it's not possible
    if MinCoins[total] == float('inf'):
        return -1

    else:
        return MinCoins[total]
