# MEDIUM
# recursion 

# recursive rule: 
#     s[i-1] == s[i] == "+" and flipped s[i-1:i+1] + rest of string are not flippable

class Solution:
   
    def canWin(self, s: str) -> bool:
        self.memo = {}
        return self.dfs(s)
    def dfs(self,s):
        if s in self.memo:
            return self.memo[s]
        tmp = False
        for i in range(1,len(s)):
            tmp = s[i-1] == "+" and s[i] == "+" and not\
                    self.dfs(s[:i-1]+"--"+s[i+1:])
            
            if tmp == True:
                return True
        self.memo[s] = tmp
        return tmp
    
    