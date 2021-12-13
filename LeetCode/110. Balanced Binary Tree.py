# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if node is None:
                return True
            elif node.left and node.right:
                child_height = max(get_height(node.left),get_height(node.right))
            elif node.left:
                child_height = get_height(node.left)
            else:
                child_height = get_height(node.right)              
            return 1+child_height
        
        if root is None:
            return True
        else:
            if abs(get_height(root.left)-get_height(root.right))<=1:
                return self.isBalanced(root.left) & self.isBalanced(root.right)
            else:
                return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or \
            abs(left-right) > 1:
                return -1
            else:
                return max(left,right) + 1
            
        return check(root) != -1
