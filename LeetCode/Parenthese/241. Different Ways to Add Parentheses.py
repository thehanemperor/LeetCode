# MEDIUM 
# this is like Word Break => DFS + Memoization 
# define a lambda x,y: x {+,-,*} y 

# scan the string s:
#     break at operators "+-*" => left = s[:operator] right = s[operator+1:]
#     recurse each left, right:

#     try every possible operations of left and right 

# Time O(N!)  Space O(N)


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        self.memo = {}
        self.ops = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
           
        }
        return self.dfs(input)
        
    def dfs(self,s):
        result = []
        
        if s in self.memo:
            return self.memo[s]
        
        for i in range(len(s)):
            if s[i] in {"+","-","*"}:
                left = s[:i]
                right = s[i+1:]
                l = self.dfs(left)
                r = self.dfs(right)
                
                for a in l:
                    for b in r:
                        result.append(self.ops[s[i]](a,b))
                        
        if not result:
            result.append(int(s))
        self.memo[s] = result
        return result
        