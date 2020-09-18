class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.gmax = -float("inf")
        self.dfs(root)
        return self.gmax
        
    def dfs(self,root):
        if not root:
            return -float("inf")
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.gmax = max(self.gmax,root.val,max(left,right) ,max(left,right)+root.val,left+right +root.val)
        # print('gmax',self.gmax)
        # print(left,right,root.val)
        return max(root.val ,max(left,right)+root.val)