# HARD 
# Use stack calculate () first and calculate as whole 
# corner case:
#     1. value after "("
#     2. when stack length == 1 => (5)
#     3. negative result 

# Time O(N)  Space O(N)

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        stack = []
        for c in s:
            if c == " ":
                continue
                
            if c == ")":
                num = self.calPart(stack)
                
                stack.append(str(num))
            else:
                stack.append(c)
        print(stack) 
        return self.calPart(stack)
                               
    def calPart(self,stack):
        if len(stack)== 1:
            return int(stack[0])
        digit = ''
        num = 0
        while stack:
            curr = stack.pop()
            
            if  curr == "(":
                num += int(digit)
                break
            else:
                if curr[0]=="-" and curr[1:].isdigit():
                    digit = curr
                elif curr.isdigit():
                    
                    digit= curr + digit
                    if not stack :
                        num +=int(digit)
                    
                else:
                    if curr == "+":
                        num+= int(digit)
                    else:
                        num -= int(digit)
                    
                    digit = ""
                    
        return num
                        