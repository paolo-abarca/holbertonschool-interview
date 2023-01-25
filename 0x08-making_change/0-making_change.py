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

    counter = 0
    tmp = 0
    coins.sort(reverse=True)

    for coin in coins:
        if coin < total:
            while tmp < total:
                tmp += coin
                if tmp <= total:
                    counter += 1
                else:
                    tmp -= coin
                    break

    if tmp == total:
        return counter

    return -1
