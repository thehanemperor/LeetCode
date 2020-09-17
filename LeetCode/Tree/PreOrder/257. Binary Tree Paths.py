class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        self.preOrder(root,[],result)
        return result
    
    def preOrder(self,root,tmp,result):
        if not root:
            return 
        if not root.left and not root.right:
            tmp.append(str(root.val))
            result.append("->".join(tmp))
            tmp.pop()
            return
        
        tmp.append(str(root.val))
        self.preOrder(root.left,tmp,result)
        self.preOrder(root.right,tmp,result)
        tmp.pop()
        
        