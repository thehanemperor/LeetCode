class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        self.iterative(root,result)
        return result
    
    def iterative(self,root,result):
        stack = [root]
        # result.append(root.val)
        while stack:
            
            while root :
                result.append(root.val)
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            root = root.right
            
            
        
            
    def dfs(self,root,result):
        if not root:
            return 
        result.append(root.val)
        self.dfs(root.left,result)
        self.dfs(root.right,result)