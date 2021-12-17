# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Search
class Solution:
    def mergeTrees(self, t1: TreeNode, t2:  TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2

#BFS
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val+=root2.val
        q1 = collections.deque([root1])
        q2 = collections.deque([root2])
        while (q1 or q2):
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1 and node2:
                if node1.left and node2.left:
                    node1.left.val+=node2.left.val
                elif node2.left:
                    node1.left=TreeNode(val=node2.left.val)
                if node1.right and node2.right:
                    node1.right.val+=node2.right.val
                elif node2.right:
                    node1.right=TreeNode(val=node2.right.val)
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
                
        return root1
