# EASY 
# 1. store the count of each digit into dict as {3:1,,,,}
# 2. loop the input and check if nums[i] -k in dict ?
#     if yes, we found one pair 



class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        check = {}
        for i in range(len(nums)):
            check[nums[i]] = check.get(nums[i],0) + 1
        appear = set([])
        result = 0
        for n in nums:
            if n-k in check :
                if n-k == n and check[n-k]<2:
                    continue
                if (n,n-k) not in appear:
                    appear.add((n,n-k))
                    appear.add((n-k,n))
                    result += 1
                    
        return result