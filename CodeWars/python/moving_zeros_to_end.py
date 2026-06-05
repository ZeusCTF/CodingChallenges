"""
Moving Zeros To The End
https://www.codewars.com/kata/moving-zeros-to-the-end
Topic: Array

Move all zeros in the array to the end while preserving the order of
non-zero elements.
"""
from typing import List


def move_zeros(array: List) -> List:
    non_zeros = [x for x in array if x != 0]
    zeros     = [x for x in array if x == 0]
    return non_zeros + zeros
