"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Topic: Linked List

Merge two sorted linked lists into one sorted linked list.

Approach: Use a dummy head node.  Compare the current nodes of both lists
and advance the pointer of whichever had the smaller value.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return dummy.next
