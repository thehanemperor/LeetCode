# MEDIUM 
# Sliding window ==> window size = p.length
# use dict {a: count, b: count,,,, z:count} denote the pattern of p 
#    ex: Input = "cbaebabacd"
#                 ___ 
#                  ___ 
#                   ___ 
#                        ___


#     Time O(N)  Space O(N)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ns,np = len(s),len(p)
        if np > ns:
            return []
        result = []
        source,pattern = [0]*26, [0]*26
        for c in p:
            pattern[ord(c)-ord('a')] += 1
        
        for i in range(ns):
            source[ord(s[i])-ord('a')]+=1
            if i>=np:
                source[ord(s[i-np])-ord('a')] -=1
            
            if source==pattern:
                result.append(i-np+1)
                
        return result
                
        