# MEDIUM
# 1. sort the intervals with i[0]
#     append index to each element 

# 2. scan intervals and look for closest greater index in sorted intervals
#     binary search look for closest value:
#         do not return inside the loop 
#         assign new greater value to the result every time when find one 
#         loop stops when left >right 

# Time O(N logN) Space O(N)
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        check = []
        result = []
        for i,v in enumerate(intervals):
            check.append([*v]+[i])
            
        
        check.sort(key = lambda x:x[0])
        print(check)
        def binSearch(end):
            ans = -1
            left,right = 0,len(check)-1
            while left<=right:
                mid = left + (right-left >>1)
                if check[mid][0]>= end:
                    ans = check[mid][2]
                    right = mid -1
                else:
                    left = mid + 1
                    
            return ans
                    
                
        for i,j in intervals:
            after= binSearch(j)
            result.append(after)
            
        return result