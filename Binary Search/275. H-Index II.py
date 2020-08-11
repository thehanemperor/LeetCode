# MEDIUM 
# because Its sorted 
#     ex: [0,1,3,5,6]
#     if we reverse the input as => [6,5,3,1,0]
#         1. first look mid, index:2, 
#                 nums[2] > index, 
#                     means we found one, but have potential larger one
#                     we move left to mid +1 and search the rest 
        
#         2. look at mid between [...,1,0]
#             mid: index = 4
#                 nums[4] < index. this one does not fit, we need check previous
#                 move right to mid -1
        
#         stop right < left 

# Time O(Log N)  Space O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right = 0, len(citations)-1
        n = len(citations)
        result = 0
        while left <= right:
            mid = left + (right-left >>1)
            print(mid,citations[mid],n-1-mid)
            if citations[mid]> n-1-mid:
                result = n-mid
                right = mid - 1
            else:
                left = mid +1
                
        return result
            