# HARD 
# 1. build a palindrome table 
# palindrome[i][j] => True if s[i:j] is palindromic else False 
# 2. dp => [MaxInt] * (n+1) represent every chunk of s 
#     dp[0] = 0 since no chunk can be splited 
#     dp[i] = min(dp[i], dp[j]+1) for j in range(i) if palindromic[j][i-1]

# Time O(N^2) Space O(N^2)

class Solution:
    def minCut(self, s: str) -> int:
        palin =self.findPalin(s)
        n = len(s)
        dp =[float("inf")]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for j in range(i):
                if palin[j][i-1]:
                    dp[i] = min(dp[i],dp[j]+1)
        
        return dp[n]-1
        
        
    def findPalin(self,s):
        dp = list(map(lambda x:[False]*len(s),range(len(s))))
        
        
        n = len(s)
        for i in range(n):
            left,right = i,i
            while left >=0 and right <n and s[left]==s[right]:
                dp[left][right] = True
                left -= 1
                right += 1
                
            left,right = i,i+1
            while left >=0 and right <n and s[left]==s[right]:
                dp[left][right] = True
                left -= 1
                right += 1
                
        return dp
                