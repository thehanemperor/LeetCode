# MEDIUM 
# two pointers as left,right boundaries
# define a hashmap or array to maintain the current state
# if right pointer not exists in map -> increment right to grow the window size 
# else -> increment the left pointer to decrease the window size 

# Time O(N) Space O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow,fast = 0,0
        n = len(s)
        appear= [0]*128
        result = 0
        while fast < n:
            if not appear[ord(s[fast])-ord("a")] :
                #print(s[slow:fast+1])
                result = max(result,fast-slow +1)
                appear[ord(s[fast])-ord("a")]+=1
                fast += 1
            else:
                if appear[ord(s[slow])-ord("a")] > 0:
                    appear[ord(s[slow])-ord("a")]-=1
                slow += 1
            
            
        return result