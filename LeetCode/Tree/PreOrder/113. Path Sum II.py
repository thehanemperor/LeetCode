class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        self.dfs(root,sum,[],result)
        return result
    def dfs(self,root,total,tmp,result):
        if not root:
            return 
        
        if not root.left and not root.right and not total -root.val:
            tmp.append(root.val)
            result.append([*tmp])
            tmp.pop()
            return 
            
        tmp.append(root.val)
        self.dfs(root.left,total-root.val,tmp,result)
        self.dfs(root.right,total-root.val,tmp,result)
        tmp.pop()
        