class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True
        self.dfs(root)
        return self.balanced
    
    def dfs(self,root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left-right)>1:
            self.balanced = False
        return max(left,right)+ 1