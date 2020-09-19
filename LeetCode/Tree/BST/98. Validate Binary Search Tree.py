class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.isBst = True
        
        return self.dfs(root,-float("inf"),float("inf"))
        
        
    def dfs(self,root,lo,hi):
        if not root:
            return True
        
        left = self.dfs(root.left,lo,root.val)
        right = self.dfs(root.right,root.val,hi)
        """
        left <root.val
        """
        print(lo,root.val,hi)
        if root.val>= hi or root.val<= lo:
            return False
        return left and right
        
        