# Given two strings s and t, determine if they are both one edit distance apart.

# Note: 

# There are 3 possiblities to satisify one edit distance apart:

# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.

# MEDIUM

# Since we can only and must edit once. these two strings.length must have differentiations <= 1 and 
#     they can not be same strings

# 3 cases:
#     1st easy one. when differentiations >1 ==> False
#     2nd when differentiations == 0:
#         check every char of two strings and count of different chars must == 1
#     3rd when differentiations == 1:
#         go over the shorter string, 
#         if we found unmatched char: 
#             ==> longer[i+1:] == shorter[i:]

# Time O(N) space O(1)


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s==t:
            return False
        if abs(len(t) - len(s))>1:
            return False
        elif len(t) == len(s):
            count = 0
            for i in range(len(t)):
                if t[i] != s[i]:
                    count+=1
            return count <= 1
        elif abs(len(t)-len(s)) == 1:
            if len(s)>len(t):
                s,t = t,s
            n = len(s)
            for i in range(n):
                if t[i] != s[i]:
                    return s[i:] == t[i+1:]
            
            return True
