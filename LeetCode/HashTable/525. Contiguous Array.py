# MEDIUM 
# find subarray of same number of 0,1 
#     1. change all 0 => -1
#     2. save prefix sum into dict{ currSum: index }
#     3.  
#         if currSum == 0:
#             result = i + 1
#         if currSum in dict:
#             get max 
#         else store currSum into dict with i 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        appear = {}
        
        curr = 0
        result = 0
        for i in range(len(nums)):
            curr += nums[i] if nums[i] else -1
            if curr == 0:
                result = i+1
            elif curr in appear:
                result = max(result,i- appear[curr])
            else:
                appear[curr] = i
                
        return result