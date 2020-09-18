# MEDIUM 
# use hashmap,
#     the leaf is lowest level, when going up, we increment the level
# Time O(N) Space O(N)
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.dict_t = defaultdict(list)
        self.dfs(root)
        
        return [[*v] for v in self.dict_t.values()]
        print(self.dict_t)
        
    def dfs(self,root):
        if not root:
            return 0
        
        depth = max(self.dfs(root.left),self.dfs(root.right))
        self.dict_t[depth].append(root.val)
        
        return depth + 1