# HARD 
# k -> at most means we need a range <= k 
# use a hashmap/array to maintain the current state

# structure of the hashmap -> {'c',last occured index}
# eg. "abaccc" k = 2
#     {'a': 0}
#     {'a': 0, 'b': 1}
#     {'a': 2, 'b': 1}
#     {'a': 2, 'b': 1, 'c': 3} -> map size >k, delete the s[min(map.values())], then increment left pointer to that position
#     {'a': 2, 'c': 3}
#     {'a': 2, 'c': 4}
#     {'a': 2, 'c': 5}
    
# Time O(N)  Space O(N)


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        
        required = 0
        count = {}
        slow,fast = 0,0
        gmax = 0
        while fast< len(s):
            c = s[fast]
            count[c] = fast
            
            if len(count)<= k:
                
                gmax = max(gmax,fast-slow+1)
            if len(count)>k:
                getRid = min(count.values())
                slow = count[s[getRid]]+1
                count.pop(s[getRid])
                
            else:
                fast += 1
            
        return gmax
    
                