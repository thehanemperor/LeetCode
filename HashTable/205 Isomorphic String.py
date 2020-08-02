# EASY
# first, we assume the lengths of both s and t are the same. if not -> False

# second, we check every char from t and save em in a hashMap as { t[i]: s[i] }

# go over s to check if the chars match what we had in hashMap

# Time O(N) space O(N)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dict_t = {}
        appear = set([])
        for i in range(len(s)):
            if t[i] not in appear:
                appear.add(t[i])
                dict_t[s[i]] = t[i]
            
        
        for i in range(len(s)):
            if s[i] not in dict_t or  dict_t[s[i]]!= t[i]:
                return False
            
            
            
        return True