import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 0ms / 17.95MB
class Solution:
    min_diff = 10**5

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def get_closest(node):
            left, right = node.left, node.right
            if left:
                while left.right:
                    left = left.right
                self.min_diff = min(self.min_diff, node.val - left.val)
            if right:
                while right.left:
                    right = right.left
                self.min_diff = min(self.min_diff, right.val - node.val)

        que = collections.deque([root])
        while que:
            node = que.popleft()
            get_closest(node)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return self.min_diff
