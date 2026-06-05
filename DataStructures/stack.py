"""
Stack
-----
Array-backed stack with standard push/pop/peek operations.

push/pop/peek: O(1) amortized
is_empty/size: O(1)

Includes a MonotonicStack helper used in histogram-type problems.
"""
from typing import TypeVar, Generic, Optional, List

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self._data: List[T] = []

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"


def is_valid_parentheses(s: str) -> bool:
    """LeetCode 20 — Valid Parentheses using the Stack above."""
    stack: Stack[str] = Stack()
    match = {"(": ")", "{": "}", "[": "]"}
    for ch in s:
        if ch in match:
            stack.push(ch)
        elif stack.is_empty() or match[stack.pop()] != ch:
            return False
    return stack.is_empty()


if __name__ == "__main__":
    s: Stack[int] = Stack()
    for v in [1, 2, 3]:
        s.push(v)
    print(s)             # Stack([1, 2, 3])
    print(s.pop())       # 3
    print(s.peek())      # 2

    print(is_valid_parentheses("()[]{}"))  # True
    print(is_valid_parentheses("(]"))      # False
    print(is_valid_parentheses("{[]}"))    # True
