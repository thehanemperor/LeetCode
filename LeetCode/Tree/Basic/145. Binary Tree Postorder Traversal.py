# MEDIUM
# Input:          1
#             /       \
#            4         5
#          /   \      / \
#         2     3    6   7

#         [1 -> 5 -> 7 -> 6 -> 4 -> 3 -> 2]
# reverse =>
#         [2 -> 3 -> 4 -> 6 -> 7 ->5 -> 1]
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.dfs(root,result)
        return result
    
    def iterative(self,root):
        if not root:
            return []
        result = []
        stack = []
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.right
        
            root = stack.pop()
            
            root = root.left
        return reversed(result)                

    def dfs(self,root,result):
        if not root:
            return 
        
        self.dfs(root.left,result)
        self.dfs(root.right,result)
        result.append(root.val)