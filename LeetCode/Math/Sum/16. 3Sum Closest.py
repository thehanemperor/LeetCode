# MEDIUM
# 3 sum + two pointer

# compare the abs(target - sum(3)) with global min 

# Time O(N^2) Space O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        gmin = float("inf")
        for i in range(len(nums)):
            
            left,right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i]+ nums[left]+ nums[right]
                if abs(target - total)< abs(gmin):
                    gmin = target - total
                if total == target:
                    break
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1

            if gmin == 0:
                break
        
        return target - gmin
            
        
            