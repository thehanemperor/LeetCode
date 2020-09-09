# HARD 

# asking for longest valid parenthese string.
# input ")()())"  => 4 because s[1:4] is the longese valid substring

# dp[N] each index represents the number of valid parenthese at that place: 

# scan the string:
#     if string[i-1:i] == "()" means we found one => dp[i] = dp[i-2] + 2 
#     elif string[i-1] != "(" check s[i - dp[i-1] -1]  and s[i] == "()"
#         => dp[i] = dp[i-1] + dp[i - dp[i-1]-2] +2  eg."()((()))"
#                                                         ^     ^
#                                                         |     |
#                                                     dp[i-dp[i-1]-2]

# Time O(N)  Space O(N)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        gmax = 0
        dp = [0]* len(s)
        for i in range(1,len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2]+2 if i>=2 else 2
                    
                elif i- dp[i-1]>0 and s[i-dp[i-1]-1]=="(":
                    dp[i]= dp[i-1]+ (dp[i-dp[i-1]-2]+2 if i-dp[i-1]>=2 else 2)
            gmax = max(gmax,dp[i])
            
        return gmax
