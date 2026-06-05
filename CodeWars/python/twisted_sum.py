"""
Twisted Sum
https://www.codewars.com/kata/twisted-sum
Topic: Math

Sum the individual digits of all integers from 1 to n inclusive.
"""


def compute_sum(n: int) -> int:
    return sum(int(d) for i in range(1, n + 1) for d in str(i))
