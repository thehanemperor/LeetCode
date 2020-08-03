# EASY
# Linear Scan look back, pop stack when "#" appear

# Time O(N) Space O(N)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
    def useStack(self,S,T)
        stack1,stack2 = [],[]
        for c in S:
            if c !="#":
                stack1.append(c)
            else:
                if stack1:
                    stack1.pop()
        
        for c in T:
            if c !="#":
                stack2.append(c)
            else:
                if stack2:
                    stack2.pop()
        
        i,j = 0,0
        while i < len(stack1) and j <len(stack2):
            if stack1[i]!=stack2[j]:
                return False
            i+=1
            j+=1
        
        if i<len(stack1) or j<len(stack2):
            return False
        
        return True