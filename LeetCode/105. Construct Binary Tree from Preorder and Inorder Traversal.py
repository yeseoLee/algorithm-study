from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 110ms / 89.84MB
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root_idx = inorder.index(root_val)

        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1 :]
        preorder_left = preorder[1 : 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left) :]

        root = TreeNode(root_val)
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
