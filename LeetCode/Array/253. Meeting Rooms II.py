# MEDIUM 
# use Heap 
# check every end-time with next start-time
# if end-time <= start-time:
#     remove end-time from heap

# push end-time to heap

# Time O(N logN) Space O(N)

from heapq import heappush,heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[0])
        
        rooms = [intervals[0][1]]
        for meeting in intervals[1:]:
            if rooms[0] <= meeting[0]:
                heappop(rooms)
                
            heappush(rooms,meeting[1])
            
        return len(rooms)
        