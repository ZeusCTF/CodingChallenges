"""
100. Same Tree
https://leetcode.com/problems/same-tree/
Difficulty: Easy
Topic: Tree, DFS

Given the roots of two binary trees p and q, return True if they are
structurally identical and every node has the same value.

Approach: DFS recursion.
  - Both None → True (base case, subtrees match)
  - Exactly one None → False (shapes differ)
  - Values differ → False
  - Otherwise recurse on left and right subtrees simultaneously
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        # Bug fix: original checked p.left twice; must compare left-left AND right-right
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
