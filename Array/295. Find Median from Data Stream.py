# HARD
# 2 heaps
#     1. maxHeap for smaller Numbers  =>  
#     2. minHeap for larger Numbers

#     maxHeap : [4,3,2,1]
#     minHeap : [5,6,7,8]

#     when look for median, just take each head, but we have to maintain the heaps balanced

#     push every number to maxHeap first because it stores smaller number, when we pop the maxHeap, we will get the largest from it 
#     append the largest value popped from maxHeap to minHeap 

#     then maintain two heaps balanced    

from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxSmall = []
        self.minLarge = []
        

    def addNum(self, num: int) -> None:
        
        heappush(self.maxSmall,-num)
        heappush(self.minLarge, -(heappop(self.maxSmall)))
        
        if len(self.maxSmall)<len(self.minLarge):
            heappush(self.maxSmall,-(heappop(self.minLarge)))
        
            
        
    def findMedian(self) -> float:
        
        length = len(self.maxSmall) + len(self.minLarge) 
        if length %2 == 0:
            
            return (-self.maxSmall[0] + self.minLarge[0]) /2 
        return -self.maxSmall[0]

