class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        self.preOrder(root,0)
        return self.result
    def preOrder(self,root,tmp):
        if not root:
            return 
        if not root.left and not root.right:
            # sum here
            self.result += tmp*10 + root.val
            # print(self.result)
            return
    
        self.preOrder(root.left,tmp*10+root.val)
        self.preOrder(root.right,tmp*10+root.val)
            
        