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

    num = 0
    for coin in sorted(coins, reverse=True):
        if total == 0:
            return num
        num += total // coin
        total %= coin

    if total == 0:
        return num

    return -1
