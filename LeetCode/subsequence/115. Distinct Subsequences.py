class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        row,col = len(t),len(s)
        dp = [[0 for _ in range(col+1)] for _ in range(row +1)]
        for j in range(col+1):
            dp[0][j] = 1
            
        for i in range(1,row+1):
            for j in range(i,col+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] +dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
            
        # for d in dp:
        #     print(d)
        return dp[row][col]
        #dp[]