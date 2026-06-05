"""
All Star Code Challenge #15
https://www.codewars.com/kata/all-star-code-challenge-15
Topic: String, Rotation

Given a string, return all rotations of it.
A rotation moves the first character to the end.

Example: "abc" → ["bca", "cab", "abc"]
"""
from typing import List


def rotate(s: str) -> List[str]:
    return [s[i:] + s[:i] for i in range(1, len(s) + 1)]
