# EASY 
# Two Pointer
#     if s[i] == t[j] both pointer increment
#     else 
#         t pointer increment 

# Time O(N) Space O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns,nt = len(s),len(t)
        slow,fast = 0,0
        while slow < ns and fast < nt:
            
            if s[slow] == t[fast]:
                slow += 1
            
            fast += 1
        
        return slow == ns