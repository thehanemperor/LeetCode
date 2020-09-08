# HARD 
# Input: "abcd"

# reverse input => as rev = "dcba"

# compare s[:n-i] with rev[i:]
#     abcd vs dcba
#     abc  vs  cba
#     ab   vs   ba
#     a    vs    a   => i == 3

#     the same substring is the overlapped part of the result, thus rev[:i] + s is the result 

# Time O(N^2) Space O(n)

# KMP prefix table 
#     this reduced the substring time to O(1)

# Time O(N) Space O(N)


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return self.slow(s)
    
    def slow(self,s):
        n = len(s)
        rev = ''.join(reversed(list(s)))
        for i in range(n):
            if s[:n-i] == rev[i:]:
                return rev[:i]+ s
            
        return ""
    def fast(self,s):
        n = len(s)
        rev = ''.join(reversed(list(s)))
        formed = s+"*"+rev
        prefix = self.buildPrefix(formed)
        # print([i for i in formed])
        # print(prefix)
        return rev[0:n-prefix[-1]]+s
        
        
    def buildPrefix(self,s):
        n = len(s)
        prefix = [0]*n
        length = 0
        i = 1
        j = 0
        while i <n:
            if s[i] == s[length]:
                length += 1
                prefix[i] = length
                i += 1
            else:
                if length> 0:
                    length = prefix[length-1]
                else:
                    prefix[i] = length
                    i+=1
                    
        return prefix