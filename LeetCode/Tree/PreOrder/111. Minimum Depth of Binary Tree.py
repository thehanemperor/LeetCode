class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.bfs(root)
        
        if not root:
            return 0
        self.gmin = float('inf')
        self.preOrder(root,1)
        return self.gmin
        
        
    def bfs(self,root):
        if not root:
            return 0
        level = 1
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr.left and not curr.right:
                    return level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            
            level += 1
            
            
        
    def preOrder(self,root,level):
        if not root.left and not root.right:
            self.gmin = min(self.gmin,level)
            
        if root.left:
            self.preOrder(root.left,level+1)
        if root.right:
            self.preOrder(root.right,level + 1)