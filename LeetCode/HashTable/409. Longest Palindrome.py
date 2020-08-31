# EASY 
# count every char in string 
# sum = each even + each (odd - 1) 
# Time O(N) Space O(N)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        appear = {}
        for c in s:
            if c in appear:
                appear[c] += 1
            else:
                appear[c] = 1
        
        result = 0
        odd = False
        for k,v in appear.items():
            if v%2== 0:
                result +=v
            else:
                odd = True
                result += v -1
                
        return result+1 if odd else result