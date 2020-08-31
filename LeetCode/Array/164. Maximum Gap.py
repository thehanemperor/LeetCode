# HARD 
# Bucket Sort ==> O(N) like partition
# Bcket object = {min = minimumValue, max = maximumValue}
# [1,5,8,4,1,968,5,6,8,456,8,4,75,96]

# we sort the input to n bucktes with range 
# min max
# 1    8,   75   96,   inf -inf,   inf -inf,   inf -inf,   inf -inf,   456 456,   inf -inf,   inf -inf,   inf -inf,   inf -inf,   inf -inf,   inf -inf,   968 968,   

# scan each bucket and compare bucket.min with previous max

class Buckets:
    def __init__(self):
        self.used = False
        self.min = float("inf")
        self.max = -float("inf")
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        mini,maxi = min(nums) , max(nums)
        bucketSize = max(1,(maxi-mini) // (n-1))
        bucketNum = (maxi - mini) // bucketSize +1
        buckets = list(map(lambda x:Buckets(),range(bucketNum)))
        
        for num in nums:
            ids = (num-mini)// bucketSize
            buckets[ids].used = True
            buckets[ids].min = min(num,buckets[ids].min)
            buckets[ids].max = max(num,buckets[ids].max)
            
        prevMax = mini
        maxGap = 0
        
        for buc in buckets:
            if not buc.used:
                continue
            maxGap = max(maxGap, buc.min - prevMax)
            prevMax = buc.max
            
        return maxGap