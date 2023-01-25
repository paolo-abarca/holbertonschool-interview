#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins: list, total: int) -> int:
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    change = 0
    coins.sort(reverse=True)

    for coin in coins:
        temp_change = int(total / coin)
        total -= temp_change * coin
        change += temp_change
        if total == 0:
            return change
    if total != 0:
        return -1
