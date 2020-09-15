# EASY 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i,v in enumerate(nums):
            if target - v in check:
                return [check[target-v],i]
            check[v] = i
            
        return []