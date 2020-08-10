
# MEDIUM
# cur records the count of "aeiou"
# cur & 1 = the records of a % 2
# cur & 2 = the records of e % 2
# cur & 4 = the records of i % 2
# cur & 8 = the records of o % 2
# cur & 16 = the records of u % 2
# seen note the index of first occurrence of cur

# 	                                        a       e       i       o       u       other
# 	"aeiou".indexOf(s.charAt(i)) + 1        1       2       3       4       5       0
# 						1 << tmp            2       4       8      16      32       1
# 				(1 << tmp) >> 1             1       2       4       8      16       0

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        result= 0
        curr = 0
        n = len(s)
        vow = "aeiou"
        seen = {0:-1}
        for i in range(n):
            curr ^= 1<< ("aeiou".find(s[i])+1) >> 1
            if curr not in seen:
                seen[curr]= i
            result = max(result,i-seen[curr])
            
        return result