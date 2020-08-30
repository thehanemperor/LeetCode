# MEDIUM 
# 1. make prefix set. prefix[i] = nums[0]+ nums[1] + nums[2] + ... + nums[i]
# 2. Recall Two Sum, dict save prefix[i] - k.
#     ex. Input: nums = [1, -1, 5, -2, 3], k = 4
#         prefix = [1, 0, 5, 3, 6]
#         when i = 2, prefix[2] = 5, ( 5-4 == prefix[0] )
#         answer = i - 0 (index of prefix[0])

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n<1:
            return 0
       
        prefix = {}
        result = 0
        curr = 0
        for i in range(n):
            curr += nums[i]
            if curr == k:
                result = i+1
            elif curr - k in prefix:
                result = max(result, i - prefix[curr-k])
            
            if curr not in prefix:
                prefix[curr] = i
        
        return result
       