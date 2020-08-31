# HARD 
# 2 dementional => dp [{}] 
# dp[i][j] => counts of sequence diff with j nums[i] have
#     ex: input = [2,4,6,8,10]
#         dp[2][6-2] = 0 + 1 
#         dp[2][6-4] = 1 + 1

# time O(N^2) space O(N^2)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        result = 0
        count = [{} for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                
                curr = count[j].get(diff,0)
                origin = count[i].get(diff,0)
                count[i][diff] = origin +curr+1
                result += curr
        
                
        return result