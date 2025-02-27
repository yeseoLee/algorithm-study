import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 0ms / 25.34MB
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if not node:
                continue
            if low <= node.val <= high:
                s += node.val
                que.append(node.left)
                que.append(node.right)
            elif node.val < low:
                que.append(node.right)
            else:
                que.append(node.left)
        return s
