class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        Fib50 = [1,1]
        
       
        
        
        if not root:
            return []
        queue = deque([root])
        result = deque([])
        
        while queue:
            tmp = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                tmp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            result.appendleft([*tmp])
            
        return result
        