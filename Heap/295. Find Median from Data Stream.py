# HARD
# max heap store=> smaller numbers [3,2,1]
# min heap store => larger number  [4,5,6]
# the median is the each top of both heaps

from heapq import heappush,heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        max heap store=> smaller numbers [3,2,1]
        min heap store => larger number [4,5,6]
        
        """
        
        self.largerMinHeap = []
        self.smallerMaxHeap = []

    def addNum(self, num: int) -> None:
        
        heappush(self.smallerMaxHeap,-num)
        
        heappush(self.largerMinHeap, -heappop(self.smallerMaxHeap))
        if len(self.smallerMaxHeap) < len(self.largerMinHeap):
            top = heappop(self.largerMinHeap)
            heappush(self.smallerMaxHeap,-top)
        
        

    def findMedian(self) -> float:
        return -self.smallerMaxHeap[0] if len(self.smallerMaxHeap) > len(self.largerMinHeap)\
                else (self.largerMinHeap[0] +(-self.smallerMaxHeap[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()