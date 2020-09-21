# MEDIUM
# inorder iterative traversal

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        pred = False
        while root or stack:
            while root:
                stack.append(root)    
                root = root.left
            
            root = stack.pop()
            if pred:
                return root
            if root == p:
                print("found pred",p.val)
                pred = True
            
            root = root.right
            
        return None