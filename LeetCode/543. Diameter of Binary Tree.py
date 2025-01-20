from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 7ms / 20.86MB
class Solution:
    answer = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(self, node):
            if not node:
                return 0

            l, r = 0, 0
            if node.left:
                l = 1 + dfs(self, node.left)
            if node.right:
                r = 1 + dfs(self, node.right)
            self.answer = max(self.answer, l + r)
            return max(l, r)

        dfs(self, root)
        return self.answer


class Solution2:
    longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest
