"""
Binary Search
-------------
Iterative binary search on a sorted array.

Time:  O(log n)
Space: O(1)

Also includes search_insert_position, which returns the index where the
target would be inserted if not found (LeetCode 35).
"""
from typing import List, Optional


def binary_search(arr: List[int], target: int) -> int:
    """Return the index of target, or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_insert_position(arr: List[int], target: int) -> int:
    """Return the index of target or the index it would occupy if inserted."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  # insertion point when not found


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print(binary_search(arr, 7))   # 3
    print(binary_search(arr, 4))   # -1
    print(search_insert_position(arr, 4))  # 2
    print(search_insert_position(arr, 0))  # 0
    print(search_insert_position(arr, 12)) # 6
