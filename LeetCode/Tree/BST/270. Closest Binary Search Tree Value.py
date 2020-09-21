class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return 0
        self.diff = float("inf")
        self.result = -1
        
        self.dfs(root,target)
        return self.result
    
    def dfs(self,root,target):
        if not root:
            return 
        
        if abs(root.val-target)< self.diff:
            self.diff = abs(root.val-target)
            self.result = root.val 
        if target> root.val:
            self.dfs(root.right,target)
            
        if target< root.val:
            self.dfs(root.left,target)