# HARD
# 1. if s1 == s2 => True 
# 2. Counter(s1) != Counter(s2) => False, we cannot get a matched result if 
#     they have different chars 
# 3. compare each two parts of s1,s2 
#     eg.  s1 = great   s2 = rgeat 
#         s1[:2] ?= s2[:2]    s1[2:] ?= s2[2:]

#     compare swaped 
#         s1[:2] ?= s2[5-2:]   s1[2:] ?= s2[:5-2]

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        for i in range(1,len(s1)):
            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])):
                return True
            
            if (self.isScramble(s1[:i],s2[len(s1)-i:]) and \
                self.isScramble(s1[i:],s2[:len(s1)-i])):
            
                return True
            
        return False