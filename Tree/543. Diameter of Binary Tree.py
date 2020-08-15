# EASY 
# may not go through the root !

# Time O(N) Space O(N)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.gmax = 0
        self.dfs(root)
        return self.gmax
        
    def dfs(self,root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.gmax = max(self.gmax,left+right)
        return max(left,right)+1