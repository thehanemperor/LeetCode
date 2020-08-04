# MEDIUM 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        print(intervals)
        slow,fast = 0,1
        while fast < len(intervals):
            if intervals[slow][1]>= intervals[fast][1]:
                fast += 1
            elif intervals[fast][0]<= intervals[slow][1]< intervals[fast][1]:
                intervals[slow][1] = intervals[fast][1]
                fast +=1
            elif intervals[fast][0]> intervals[slow][1]:
                slow +=1
                intervals[slow] = [x for x in intervals[fast]]
                fast +=1
                
        return intervals[:slow+1]
            