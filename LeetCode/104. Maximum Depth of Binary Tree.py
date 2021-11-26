'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
#BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        que=collections.deque([root])
        depth=0
        
        while que:
            depth+=1
            for _ in range(len(que)):
                cur_root=que.popleft()
                if cur_root.left:
                    que.append(cur_root.left)
                if cur_root.right:
                    que.append(cur_root.right)
        return depth

#DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_d=[0]
        def dfs(node,d):
            max_d[0]=max(max_d[0],d)
            if node.left:
                dfs(node.left,d+1)
            if node.right:
                dfs(node.right,d+1)
        
        if root:
            dfs(root,1)
        return max_d[0]
