# HARD 

# path should include both  [parent child] 

# Time O(N) Space O(N)

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.gmax = -float('inf')
        self.dfs(root)
        return self.gmax
    
    def dfs(self,root):
        if not root:
            return -float('inf')
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        maxChild = max(left,right)
        
        self.gmax = max(self.gmax,root.val,maxChild,root.val+maxChild,root.val+left+right)
        return max(root.val,root.val+maxChild)