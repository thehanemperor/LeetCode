# HARD

# this is kinda similar to the add left,right parentheses 
# 1. find the number of invalid "(" and ")". 
#     loop the string s:
#         if curr is "(" => left counter += 1
#         else 
#             if left counter >0: means we have a "(" then left counter -= 1
#             else means we have a redundant ")" => right counter += 1

# 2. when dfs: 
#     # move forward if the next index is same. this saves alot time
#     while index+1 < len(s) and s[index+1] == s[index]:
#         index += 1

# Time O(N!) Space O(N)

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l,r = 0,0
        for p in s:
            if p == "(":
                l += 1
            if l>0:
                if p == ")":
                    l -= 1
            else:
                if p == ")":
                    r += 1
        print("left",l,"right",r)
        result = []
        self.dfs(0,l,r,s,result)
        return result
        
    def dfs(self,index,l,r,s,result):
        if l == 0 and r == 0:
            if self.isValid(s):
                result.append(s)
            return
        
        while index < len(s):
        
            if r >0 and s[index]== ")":
                
                self.dfs(index,l,r-1,s[:index]+s[index+1:],result)
                # move forward if the next index is same
                while index+1 < len(s) and s[index+1] == s[index]:
                    index += 1

            if l > 0 and s[index] == "(":
                self.dfs(index,l-1,r,s[:index]+s[index+1:],result)
                while index+1 < len(s) and s[index+1] == s[index]:
                    index += 1
                
            index += 1
    def isValid(self,s):
        stack = []
        for p in s:
            if p == ")":
                if not stack:
                    return False
                tmp = stack.pop()
                if tmp != "(":
                    return False
            elif p == "(":
                stack.append(p)
                
        return not stack
                
            
        