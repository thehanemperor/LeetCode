# MEDIUM
#  Problem asking for "How many WAYS" at the last Index
#   Example Input= [1,2,2,6]   Output = 5
#         1=>  1,2,2,6
#         2=>  1,2,26
#         3=>  1,22,6
#         4=>  12,2,6
#         5=>  12,26
#  the current Index will always have one way, which == [index-1] ways. ex. 1,2 => 1,2,6
#      if current Index and [Index-1] can be combined as a number >9 and <27 
#         we have to add [Index-2] ways. thus, [index-1] + [index - 2]

#  corner case ==> 0

# Time O(N) Space O(N)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] !="0" else 0
        for i in range(1,len(s)):
            if s[i] == "0":
                if s[i-1] =="0":
                    dp[i+1] = 0
                elif int(s[i-1])>2:
                    return 0
                else:
                    dp[i+1] =dp[i-1]
            else:
                if 10<= int(s[i-1]+s[i])<27:
                    dp[i+1]=dp[i]+dp[i-1]
                else:
                    dp[i+1] = dp[i]
            
        return dp[-1]