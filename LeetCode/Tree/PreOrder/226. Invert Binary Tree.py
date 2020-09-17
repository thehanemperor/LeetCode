class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.bfs(root)
        return self.dfs(root)
    
    def bfs(self,root):
        if not root:
            return root
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root
    
    def dfs(self,root):
        if not root:
            return 
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        root.left = right
        root.right = left
        
        return root