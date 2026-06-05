"""
112. Path Sum
https://leetcode.com/problems/path-sum/
Difficulty: Easy  Topic: Tree, DFS

Return True if the tree has a root-to-leaf path whose values sum to targetSum.

Approach: DFS accumulating the running sum; check at leaf nodes.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], running: int) -> bool:
            if not node:
                return False
            running += node.val
            if not node.left and not node.right:
                return running == targetSum
            return dfs(node.left, running) or dfs(node.right, running)
        return dfs(root, 0)
