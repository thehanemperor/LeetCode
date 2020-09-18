# MEDIUM
# if lower level has larger value, send lower value as current level
# eg.
#     send 1 to parent instead of -5 + None 
#             -5
#           /   \
#          0     1
#              /   \
#             None None     

class Solution:
    def rob(self, root: TreeNode) -> int:
       
        tmp = self.dfs(root)
        return max(tmp)
        
    def dfs(self,root):
        if not root:
            return (0,0)
        
        left,nextLeft = self.dfs(root.left)
        right,nextRight = self.dfs(root.right)
        children = max(max(nextLeft,nextRight),nextLeft + nextRight)
        
        # with curr max
        # without curr max
        return max(children,root.val+children,max(max(left,right),left+ right)), max(max(left,right),left+ right)