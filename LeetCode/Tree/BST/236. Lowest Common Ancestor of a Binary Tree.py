class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q)
    
    def dfs(self,root,p,q):
        if not root or root == p or root == q:
            # if root:
            #     print(root.val)
            return root
        
        left = self.dfs(root.left,p,q)
        right = self.dfs(root.right,p,q)
        
        if left and right:
            return root
        
        if not left and not right:
            return None
        
        elif not right:
            return left
        elif not left:
            return right