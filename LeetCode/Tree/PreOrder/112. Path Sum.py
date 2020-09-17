class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        
        return self.preOrder(root,sum)
        
    def preOrder(self,root,total):
        
        if root and not root.left and not root.right:
            #print(total,root.val)
            if total - root.val == 0:
                return True
        if not root:
            
            return False
        
        
        
        left = self.preOrder(root.left,total-root.val)
        right = self.preOrder(root.right, total-root.val)
        return left or right