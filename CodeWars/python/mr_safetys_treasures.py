"""
Mr. Safety's Treasures
https://www.codewars.com/kata/mr-safety-treasures
Topic: String, Phone Keypad

Convert each letter to its phone keypad digit.
a-c→2, d-f→3, g-i→4, j-l→5, m-o→6, p-s→7, t-v→8, w-z→9
Non-letter characters are ignored.
"""

_KEYPAD = {c: str(d) for d, letters in [
    (2, "abc"), (3, "def"), (4, "ghi"), (5, "jkl"),
    (6, "mno"), (7, "pqrs"), (8, "tuv"), (9, "wxyz")
] for c in letters}


def unlock(message: str) -> str:
    return "".join(_KEYPAD[c] for c in message.lower() if c in _KEYPAD)
