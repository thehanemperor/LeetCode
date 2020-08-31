# HARD 
# store every element into a set 
# go through the input as nums[i]:
#     if nums[i-1] or nums[i+1] in set:
#         check nums[i-1-1] or nums[i+1+1] in set ...

# keep track of longest length 
# delete from set after found one, thus there is no additonal search 
# TIME O(N) Space O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        gmax = 0
        for n in nums:
            curr = 0
            if n in check:
                curr += 1
                left,right = n-1,n+1
                while left in check:
                    curr += 1
                    check.remove(left)
                    left -= 1
                while right in check:
                    curr += 1
                    check.remove(right)
                    right += 1
                    
            gmax = max(gmax,curr)
            
        return gmax