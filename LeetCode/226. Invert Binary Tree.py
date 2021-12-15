# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
            return root
        return None

#BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left,node.right=node.right,node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

#DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                node.left,node.right=node.right,node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

#DFS(Post-Order)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                node.left,node.right=node.right,node.left
        return root
