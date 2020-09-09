# EASY
# use Stack 
# scan the String s:
#     append all left brackets {, (, [ to the stack 
#     if right brackets ],),} appear pop the stack and compare left and right 

# Time O(N) Space O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
                    ")":"(",
                    "}":"{",
                    "]": "[",
        }
        
        stack = []
        for c in s:
            #print(stack)
            if c in paren:
                if not stack:
                    return False
                tmp = stack.pop()
                #print(tmp,"c:",c)
                if tmp!= paren[c]:
                    return False
            else:
                stack.append(c)
            
        return not stack
                
            