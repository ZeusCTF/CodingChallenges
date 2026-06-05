"""
Break camelCase
https://www.codewars.com/kata/break-camelcase
Topic: String, Regex

Insert a space before each uppercase letter.
"""


def solution(s: str) -> str:
    return "".join(" " + c if c.isupper() else c for c in s)
