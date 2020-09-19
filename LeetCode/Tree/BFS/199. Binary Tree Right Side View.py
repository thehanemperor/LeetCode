class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.result = []
        self.dfs(root,0)
        return self.result
        
    def dfs(self,root,level):
        if not root:
            return 
        if len(self.result) == level:
            self.result.append(root.val)
        
    
        
        self.dfs(root.right,level+1)
        self.dfs(root.left,level+1)