# HARD 
# De Bruijn sequence
#     ex input = [0,1,2,3] sequence size = 2
#         sequence => {00, 01,02,03,10,11,12,13,20....}
#         dfs look for the sequence 
        
# Time O(n k^n) Space O(n k^n)

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n ==1 and k ==1:
            return "0"
        check = set([])
        result = []
        start = "0" * (n-1)
        print('start',start)
        self.dfs(start,k,result,check)
        result.append(start)
        
        return ''.join(result)
        
    def dfs(self,node,k,result,check):
        for i in range(k):
            nei = node + str(i)
            if nei not in check:
                
                check.add(nei)
                
                self.dfs(nei[1:],k,result,check)
                result.append(str(i))