"""
Array.diff
https://www.codewars.com/kata/array-dot-diff
Topic: Array

Remove all values in b from array a.
"""
from typing import List


def array_diff(a: List, b: List) -> List:
    remove = set(b)
    return [x for x in a if x not in remove]
