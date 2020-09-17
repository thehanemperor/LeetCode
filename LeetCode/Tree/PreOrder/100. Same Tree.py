class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.preorder(p,q)
    def preorder(self,p,q):
        if not p or not q:
            return p == q 
        
        if p.val != q.val:
            return False
        
        return self.preorder(p.left,q.left) and self.preorder(p.right,q.right) 