# MEDIUM 
# sliding window size: [Start,i]
#     increment start if window size - most frequent char > k 

# time O(N) Space O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]* 26 
        result,gmax,start = 0,0,0
        for i in range(len(s)):
            count[ord(s[i])-ord('A')]+= 1
            gmax = max(gmax,count[ord(s[i])-ord('A')])
            while i -start +1 - gmax >k:
                count[ord(s[start])-ord('A')]-=1
                start += 1
            result = max(result,i-start +1)
            
        return result