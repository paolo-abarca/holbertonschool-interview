#!/usr/bin/python3
"""
Given a set of consecutive integers starting from 1 up to and
including n, they take turns choosing a prime number from the set and
removing that number and its multiples from the set.
The player that cannot make a move loses the game
"""


def isWinner(x, nums):
    """
    function that determines who is the winner of the X games
    """
    if x is None or len(nums) == 0:
        return None

    maria = 0
    ben = 0

    for i in range(x):
        list_n = list(range(1, nums[i] + 1))
        list_n = [n for n in list_n if isCousin(n)]
        if len(list_n) == 0:
            ben += 1
        elif len(list_n) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    return "Ben"


def isCousin(number):
    """
    function that determines if a number is prime
    """
    if number < 2:
        return False

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False

    return True
