# HARD 

# 1. define a Counter and length which represents as -> Counter({'A': 1, 'B': 1, 'C': 1}) length of counter 3
# 2. create dummy variable check {}, formed = 0
# 3. two pointers {slow,fast} -> boundaries of left,right side 
#     state transformation: when formed = length -> we found a potential solution 
#                           repeatly increment slow to find an optimal window 

# eg. Input: S = "ADOBECODEBANC", T = "ABC"
#     Output: "BANC"
#     0 ADOBEC    -> decrement the window size then we have DOBEC == False
#     1 DOBECODEBA
#     2 OBECODEBA
#     3 BECODEBA
#     4 ECODEBA
#     5 CODEBA
#     6 ODEBANC
#     7 DEBANC
#     8 EBANC
#     9 BANC

# Time O(N) Space O(T)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # tracking/standard counters
        count , check = {}, Counter(t)
        # satised number of char
        formed , required = 0, len(check)
        # store currently lowest window
        result = (float("inf"),0,0)
        # boundaries
        slow,fast = 0,0
        
        while fast < len(s):
            c = s[fast]
            count[c] = count.get(c,0)+ 1
            if c in check and check[c] == count[c]:
                # one char satisfied
                formed +=1
            while formed == required and slow <= fast:
                #print(s[slow:fast+1])
                if fast - slow + 1 < result[0]:
                    result = (fast - slow + 1, slow, fast)
                # remove the first char in window
                count[s[slow]] -= 1
                # check if removed char affected result
                formed -= 1 if s[slow] in check and count[s[slow]] < check[s[slow]] \
                            else 0
                slow += 1
            
            fast += 1
            
        return s[result[1]:result[2]+1] if result[0] != float("inf") else ""