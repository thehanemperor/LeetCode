# MEDIUM 

# 1. leaf is a univalue 
# 2. if leaf and parent have same value, count ++
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    def dfs(self,root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            self.count += 1
            return True
        
        uni = True
        if root.left:
            uni = self.dfs(root.left) and uni and root.val == root.left.val
        if root.right:
            uni = self.dfs(root.right) and uni and root.val == root.right.val
            
        
        self.count += int(uni)
        return uni