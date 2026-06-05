"""
67. Add Binary
https://leetcode.com/problems/add-binary/
Difficulty: Easy  Topic: Binary, Math

Add two binary strings and return the result as a binary string.

Approach: Process digits right-to-left with a carry, similar to grade-school
addition.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry = "", 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            da = int(a[i]) if i < len(a) else 0
            db = int(b[i]) if i < len(b) else 0
            total = da + db + carry
            res = str(total % 2) + res
            carry = total // 2
        if carry:
            res = "1" + res
        return res
