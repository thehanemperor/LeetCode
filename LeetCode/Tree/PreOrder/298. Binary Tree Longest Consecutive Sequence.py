class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.gmax = 0
        self.preOrder(root,0,0)
        
        return self.gmax
    
    def preOrder(self,root,parent,level):
        if not root:
            return 
        if root.val- parent == 1:
            level += 1
        else:
            level = 1
        self.gmax = max(self.gmax,level)    
        self.preOrder(root.left,root.val,level)
        self.preOrder(root.right,root.val,level)
        