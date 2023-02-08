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
    if x is None or nums is None or x < 1 or nums == [] or type(x) != int:
        return None

    maria = 0
    ben = 0

    for i in range(x):
        list_n = list(range(2, nums[i] + 1))
        list_n = [n for n in list_n if isPrimes(n)]
        if list_n == []:
            ben += 1
        elif len(list_n) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    return None


def isPrimes(number):
    """
    function that determines if a number is prime
    """
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
