#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    MinCoins = [float('inf')] * (total + 1)
    MinCoins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                MinCoins[i] = min(MinCoins[i], 1 + MinCoins[i - coin])
    if MinCoins[total] == float('inf'):
        return -1

    else:
        return MinCoins[total]
