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

    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    return count if total == 0 else -1
