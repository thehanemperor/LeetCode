# HARD 
# Rolling Hash Method 
# abc ==> a *26^2, b * 26^1, c * 26^0. 
#     ex: 123 ==> 1*10^2, 2 * 10^1, 3 * 10^0

# we find every possible substring to find if exist a duplicated one
# start with mid, if possible ==> find longer one else find shorter one

# Time O(NlogN) Space: O(N)

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(S[i])- ord('a') for i in range(n)]
        a = 26
        mod = 2**32
        #print(nums)
        left,right = 1,n
        while left <=right:
            mid = left +(right-left >>1)
            if self.match(mid,a,mod,n,nums) != -1:
                left = mid +1
            else:
                right = mid -1
        start = self.match(mid-1,a,mod,n,nums)
        return S[start:start+left -1]
                
    def match(self,mid,a,mod,n,nums):
        h = 0
        print('mid',mid)
        for i in range(mid):
            h = (h*a + nums[i])% mod
            print(i,nums[i],h)
        seen = set([h])
        aMid = pow(a,mid,mod)
        for i in range(1,n-mid+1):
            h = (h*a - nums[i-1] *aMid + nums[i+mid-1]) % mod
            if h in seen:
                return i
            seen.add(h)
        return -1
        
    