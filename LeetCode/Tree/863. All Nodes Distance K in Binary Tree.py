# MEDIUM 

# build an undirected graph and do bfs/dfs find the path
# Time O(N)  Space O(N)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = self.buildGraph(root)

        
        result = []
        appear = set([])
        queue = deque([(target,0)])
        while queue:
            curr,dist = queue.popleft()
            appear.add(curr)
            if dist == K:
                result.append(curr.val)
            if dist < K:
                for nei in graph[curr]:
                    
                    if nei not in appear:
                        appear.add(nei)
                        queue.append((nei,dist+1))
                    
        return result
            
        
    def buildGraph(self,root):
        graph = defaultdict(list)
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                graph[curr].append(curr.left)
                graph[curr.left].append(curr)
                
            if curr.right:
                queue.append(curr.right)
                graph[curr].append(curr.right)
                graph[curr.right].append(curr)
                
        return graph
            