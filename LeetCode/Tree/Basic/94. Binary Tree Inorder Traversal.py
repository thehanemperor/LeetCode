class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        # self.dfs(root,result)
        return self.iterative(root)
        return result
        
        
    def iterative(self,root):
        if not root:
            return []
        result = []
        stack = []
        while root or stack:
            while root:
                # result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            
            root = root.right
        return result
            
    def dfs(self,root,result):
        if not root:
            return 
        self.dfs(root.left,result)
        result.append(root.val)
        self.dfs(root.right,result)