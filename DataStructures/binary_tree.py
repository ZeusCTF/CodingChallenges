"""
Binary Tree
-----------
Node definition with DFS (preorder, inorder, postorder) and BFS traversals.

DFS traversals: O(n) time, O(h) space where h = tree height
BFS traversal:  O(n) time, O(n) space
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: Optional[TreeNode]) -> List[int]:
    """Root → Left → Right"""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: Optional[TreeNode]) -> List[int]:
    """Left → Root → Right  (gives sorted order for a BST)"""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: Optional[TreeNode]) -> List[int]:
    """Left → Right → Root"""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def bfs(root: Optional[TreeNode]) -> List[List[int]]:
    """Level-order traversal; returns a list of levels."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result


def height(root: Optional[TreeNode]) -> int:
    """Return the height (max depth) of the tree."""
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3))
    print("Preorder: ", preorder(root))   # [1, 2, 4, 5, 3]
    print("Inorder:  ", inorder(root))    # [4, 2, 5, 1, 3]
    print("Postorder:", postorder(root))  # [4, 5, 2, 3, 1]
    print("BFS:      ", bfs(root))        # [[1], [2, 3], [4, 5]]
    print("Height:   ", height(root))     # 3
