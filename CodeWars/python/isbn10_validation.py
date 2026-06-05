"""
ISBN-10 Validation
https://www.codewars.com/kata/isbn-10-validation
Topic: String, Math

An ISBN-10 is valid if the weighted sum of its 10 digits (multiplied by
their position 1..10) is divisible by 11.  The last character may be 'X'
representing 10.
"""


def valid_ISBN10(isbn: str) -> bool:
    if len(isbn) != 10:
        return False
    total = 0
    for i, ch in enumerate(isbn):
        if i == 9 and ch == "X":
            val = 10
        elif ch.isdigit():
            val = int(ch)
        else:
            return False
        total += val * (i + 1)
    return total % 11 == 0
