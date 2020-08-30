# MEDIUM
# the question is asking for the patterns in "a", "za", "ab", "abc","bc"....
# the Ascii value should have difference as 1 or 25=> "za"
# create count[26] => 'a': int(times), 'b': int(times)
# increment when s[i]and s[i-1] have diff ==1
# else count[s[i]] =1

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        count = [0 for _ in range(26)]
        
        curr = 0
        for i in range(len(p)):
            if i>0 and (ord(p[i])-ord(p[i-1])==1 or ord(p[i-1])-ord(p[i])==25):
                curr += 1
            else:
                curr = 1
            count[ord(p[i])-ord('a')] = max(count[ord(p[i])-ord('a')],curr)
            
        
        return sum(count)