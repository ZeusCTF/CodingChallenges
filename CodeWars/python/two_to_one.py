"""
Two to One
https://www.codewars.com/kata/two-to-one
Topic: String, Set

Return a string containing the unique letters from both input strings,
sorted alphabetically.
"""


def longest(a: str, b: str) -> str:
    return "".join(sorted(set(a + b)))
