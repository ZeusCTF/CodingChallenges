"""
Singly Linked List
------------------
Node definition with common operations: append, prepend, delete, reverse,
find, and Floyd's cycle detection.

All operations: O(n) time unless noted; O(1) extra space.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None

    def append(self, val: int) -> None:
        """Add a node at the tail.  O(n)"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, val: int) -> None:
        """Add a node at the head.  O(1)"""
        self.head = ListNode(val, self.head)

    def delete(self, val: int) -> bool:
        """Remove the first node with the given value.  O(n)"""
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    def reverse(self) -> None:
        """Reverse the list in-place.  O(n) time, O(1) space"""
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def has_cycle(self) -> bool:
        """Floyd's tortoise-and-hare cycle detection.  O(n) time, O(1) space"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def to_list(self) -> list:
        result, curr = [], self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def __repr__(self) -> str:
        return " -> ".join(str(v) for v in self.to_list())


if __name__ == "__main__":
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)
    print("Original: ", ll)          # 1 -> 2 -> 3 -> 4 -> 5
    ll.delete(3)
    print("After del 3:", ll)        # 1 -> 2 -> 4 -> 5
    ll.prepend(0)
    print("After prepend 0:", ll)    # 0 -> 1 -> 2 -> 4 -> 5
    ll.reverse()
    print("Reversed:", ll)           # 5 -> 4 -> 2 -> 1 -> 0
    print("Has cycle:", ll.has_cycle())  # False
