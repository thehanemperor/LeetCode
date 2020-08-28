# HARD
# use Deque 
# define a deque that maintains largest num at deque head
# clean deque process:
#     pop the head when head is not in current window 
#     pop the tail if tail is less than current index 

# Time O(N) clean deque overall O(N)  Space O(N)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque([])
        def cleanDeq(i):
            if queue and queue[0] == i-k:
                
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
        
        maxId = 0
        for i in range(k):
            cleanDeq(i)
            queue.append(i)
            if nums[i]> nums[maxId]:
                maxId = i
        
        result = [nums[maxId]]
        for i in range(k,len(nums)):
            cleanDeq(i)
            queue.append(i)
            result.append(nums[queue[0]])
            
        return result