# EASY 
# count each element in array and store in dict{}
# loop through the array check if exist nums[i]+1 in dict{}


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        appear = {}
        for i in range(n):
            appear[nums[i]] = appear.get(nums[i],0) + 1
        
        result = 0
        for k,v in appear.items():
            if k+1 in appear:
                result = max(result,v+appear[k+1])
                
        
        return result