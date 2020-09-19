class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            p,q = q,p
        
        return self.dfs(root,p,q)
        
    def dfs(self,root,p,q):
        if not root or root == p or root == q:
            return root
        
        if p.val <root.val<q.val:
            return root
        
        elif p.val<root.val and q.val<root.val:
            return self.dfs(root.left,p,q)
        else:
            return self.dfs(root.right,p,q)