# MEDIUM 
# 2 method 
#     1. prefix, suffix array
#         prefix stores minimum value at the left of nums[i]
#         suffix stores maximum value at the right of nums[i]
#         go over nums and compare prefix[i]< nums[i] < suffix[i]

#     Time O(N) Space O(N)

#     2. two pointer
#         first, second == smallest, second largest
#          go over the nums and check 
#             if first <= nums[i] then assign the nums[i] to first
#             elif second <= nums[i] then assign the nums[i] to second 

#             otherwise we found a possible solution

#         since we always check first <= nums[i] first, first will always be smallest

#     Time O(N) Space O(1)

def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for third in nums:
            if third <= first:
                first = third
            elif third <= second:
                second = third
            else:
                return True
            
        return False