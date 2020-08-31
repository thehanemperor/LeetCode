# HARD 
# this is like insert Interval
# since we only add one number each time, define a newInterval[number,number] 
# we scan the existed array[start,end]
# if newInterval[1] +1 < start --> do nothing
# elif end +1 < newInterval[0] --> record the index so we can insert it later
# else time to merge intervals 

# Time O(N)  Space O(N)
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals= []
        

    def addNum(self, val: int) -> None:
        newInterval = [val,val]
        result = []
        curr = 0
        for start,end in self.intervals:
            if  newInterval[1]+1 < start:
                result.append([start,end])
            elif newInterval[0]> end + 1 :
                result.append([start,end])
                curr +=1
            else:
                newInterval = [min(newInterval[0],start),max(newInterval[1],end)]
                
        result.insert(curr,[*newInterval])
        self.intervals = result
                

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()