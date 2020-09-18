class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        return self.dfs(root,0)
        
    def dfs(self,root,level):
        if not root:
            return level        
        left = self.dfs(root.left,level+1)
        right = self.dfs(root.right,level+1)
        return max(left,right)
        