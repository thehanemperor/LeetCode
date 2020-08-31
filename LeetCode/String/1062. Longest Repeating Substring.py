# HARD
# Same logic with 1044

class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        base = 26
        nums = [ ord(S[i]) - ord('a') for i in range(n)]
        mod = 2**32
        left, right = 0, n-1
        while left<=right:
            mid = left + (right-left >>1)
            if self.match(mid,n,nums) != -1:
                left = mid +1
            else:
                right = mid -1
        
        return left -1
            
    
    def match(self,mid,n,nums):
        base = 26
        mod = 2**32
        h = 0
        for i in range(mid):
            h = (h*base + nums[i])% mod
            
        seen = set([h])
        baseMid = pow(base,mid,mod)
        for i in range(1,n-mid+1):
            # nums[i+mid-1] ==> the new added value, ^0 because its at the tail
            # rest of vals in h should be multiplied by base because all moved one to left
            h = (h*base - nums[i-1]*baseMid + nums[i+mid-1]) % mod
            if h in seen:
                return i
            seen.add(h)
            
        return -1
        