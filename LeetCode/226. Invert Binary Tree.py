import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 0ms / 17.68MB
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            que.append(node.left)
            que.append(node.right)
        return root


# Recursion
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = (
                self.invertTree(root.right),
                self.invertTree(root.left),
            )
            return root
        return None


# BFS
class Solution3:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root


# DFS
class Solution4:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root


# DFS(Post-Order)
class Solution5:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left
        return root
