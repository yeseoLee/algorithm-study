class Solution:
    longest=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left+right+2)
            return max(left,right)+1
        
        dfs(root)
        return self.longest
