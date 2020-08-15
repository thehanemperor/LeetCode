MEDIUM 
bfs ==> take the last element of the level
dfs ==> direction - right -> left, if not right, take left node 

Time O(N)  Space O(N)

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dfsResult = []
        self.dfs(root,0,dfsResult)
        return dfsResult
        return self.bfs(root)
    
    def dfs(self,root,index,result):
        if not root:
            return
        if index == len(result):
            result.append(root.val)
        
        if root.right:
            self.dfs(root.right,index+1,result)
        if root.left:
            self.dfs(root.left,index+1,result)
        
    
    
    def bfs(self,root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == size -1:
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
                    
        return result