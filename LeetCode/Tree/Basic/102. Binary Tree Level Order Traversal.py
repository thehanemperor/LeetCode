class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.levels=[]
        self.dfs(root,0)
        return self.levels
        return self.bfs(root)
    
    
    def dfs(self,root,level):
        if not root:
            return
        if len(self.levels) == level:
            self.levels.append([])
            
        self.levels[level].append(root.val)
        self.dfs(root.left,level+1)
        self.dfs(root.right,level+1)
    
    def bfs(self,root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            tmp = []
            for i in range(len(queue)):
                
                curr = queue.popleft()
                tmp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append([*tmp])
            
        return result