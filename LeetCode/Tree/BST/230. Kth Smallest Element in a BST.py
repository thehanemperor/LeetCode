# MEDIUM 
# inorder traversal using iterative 
# Time O(N) Space O(H)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.iterative(root,k)
        self.index= 1
        self.result = -1
        self.inOrder(root,k)
        return self.result
    
    def iterative(self,root,k):
        stack = []
        i = 1
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            curr = stack.pop()
            # print(curr.val)
            if i == k:
                return curr.val
            i += 1
            if curr.right:
                root = curr.right
                
            
        
    def inOrder(self,root,k):
        if not root:
            return 
        
        self.inOrder(root.left,k)
        # print(root.val,self.index)
        if self.index == k:
            self.result = root.val
             
        self.index += 1
        
        self.inOrder(root.right,k)