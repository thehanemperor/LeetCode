# MEDIUM 
# combination == DFS  
#     base case: 
#         left brakets == n and right brakets == n
    
#     recursion Rule: 
#         append left if left < n 
#         append right if left > right 

# Time O(2^N) Space O(N)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n,0,0,[],result)
        return result
        
    def dfs(self,n,left,right,tmp,result):
        if left == n and right == n:
            result.append("".join(tmp))
            return
        
        if left < n:
            tmp.append("(")
            self.dfs(n,left+1,right,tmp,result)
            tmp.pop()
            
        if left > right:
            tmp.append(")")
            self.dfs(n,left,right+1,tmp,result)
            tmp.pop()