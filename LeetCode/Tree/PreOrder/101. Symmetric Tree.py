# EASY 
# Same logic with same tree

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root,root)
        
        
    def dfs(self,r1,r2):
        if not r1 or not r2:
            return r1 == r2
        if r1.val != r2.val:
            return False
        return self.dfs(r1.left,r2.right) and self.dfs(r1.right,r2.left)
