"""
Consecutive Strings
https://www.codewars.com/kata/consecutive-strings
Topic: String

Given an array of strings and an integer k, return the longest string
formed by concatenating k consecutive strings from the array.
"""
from typing import List


def longest_consec(strarr: List[str], k: int) -> str:
    if not strarr or k <= 0 or k > len(strarr):
        return ""
    candidates = [
        "".join(strarr[i:i + k])
        for i in range(len(strarr) - k + 1)
    ]
    return max(candidates, key=len)
