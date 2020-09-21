# HARD 
# keep track of a previous node, and two more dummy node 

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def iterative(root):
            stack = []
            x = y = prev = None
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                    
                root = stack.pop()
                if prev and root.val < prev.val:
                    y = root
                    if not x:
                        x = prev
                    else:
                        
                        break
                prev = root
                root = root.right
                
            x.val,y.val = y.val,x.val
                    
        iterative(root)    
        