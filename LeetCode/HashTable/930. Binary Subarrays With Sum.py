# MEDIUM 

# prefix SUM 
# ex. input =>    [1, 0, 1, 0, 1] tar =>2
#     prefix = [0, 1, 1, 2, 2, 3]
#               |________|
#               0+2
#                  |___________|
#                  1+2    
#     go through prefix save dict{prefix[i] + tar : count }

# Time O(N)  Space O(N)

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        prefix = [0]*(n+1) 
        curr = 0
        result =0
        for i in range(1,n+1):
            curr += A[i-1]
            prefix[i] = curr
            
        count = {}
        for p in prefix:
            result += count.get(p,0)
            count[p+S] = count.get(p+S,0) + 1
            
           
        return result
        
        