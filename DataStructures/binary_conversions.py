"""
Binary Conversions
------------------
Manual decimal ↔ binary conversions without using bin() or int(x, 2).

Demonstrates bit manipulation via arithmetic.
"""


def decimal_to_binary(n: int) -> str:
    """
    Convert a non-negative integer to its binary string representation.
    Repeatedly extract the least-significant bit with n % 2, then shift
    right with n //= 2.
    """
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))


def binary_to_decimal(binary: str) -> int:
    """
    Convert a binary string to a decimal integer.
    Enumerate bits from the right; each '1' contributes 2**position.
    """
    result = 0
    for i, bit in enumerate(reversed(binary)):
        if bit == "1":
            result += 2 ** i
    return result


def find_complement(n: int) -> int:
    """
    LeetCode 476 — flip all bits in the binary representation of n.
    Uses a bitmask of all 1s with the same bit-length as n.
    """
    mask = (1 << n.bit_length()) - 1
    return n ^ mask


if __name__ == "__main__":
    print(decimal_to_binary(13))    # "1101"
    print(decimal_to_binary(0))     # "0"
    print(binary_to_decimal("1101"))  # 13
    print(binary_to_decimal("1011"))  # 11
    print(find_complement(5))       # 2  (101 → 010)
    print(find_complement(1))       # 0  (1 → 0)
