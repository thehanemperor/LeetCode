# HARD 
# logic => parse the current level and go deeper and return
# ex. Input = "(let x 1 y 2 (add x (add x y)))"
#     token =>
#         ['x', '1', 'y', '2', '(add x (add x y))']  first parsing,
#         ['x', '(add x y)']
#         ['x', 'y']

#     check the command Let => assign token pairs to scope 
#                       Mult => token[0] * token[1]
#                       add => token[0] + token[1]
# time O(N^2) Space O(N)


class Solution:
    def __init__(self):
        self.scope = [{}]
    def evaluate(self, expression: str) -> int:
        
        self.scope.append({})
        ans = self.dfs(expression)
        self.scope.pop()
        return ans
        
        
    def dfs(self,expr):
        if expr[0]!= "(":
            if expr[0].isdigit() or expr[0] == "-":
                return int(expr)
            for i in range(len(self.scope)-1,-1,-1):
                if expr in  self.scope[i]:
                    return self.scope[i][expr]
                
        if expr[1] == "m":
            # start with mult
            token = self.parse(expr[6:len(expr)-1])
        else:
            # start with add,let
            token = self.parse(expr[5:len(expr)-1])
        print(token)
        if expr.startswith("add",1):
            
            return self.evaluate(token[0]) + self.evaluate(token[1])
        elif expr.startswith("mult",1):
            return self.evaluate(token[0]) * self.evaluate(token[1])
        else:
            for j in range(1,len(token),2):
                self.scope[-1][token[j-1]] = self.evaluate(token[j])
            
            return self.evaluate(token[-1])
        
        
    def parse(self,expr):
        ans = []
        bal = 0
        buf = []
        for token in expr.split(" "):
            for char in token:
                if char == "(":
                    bal+=1
                if char == ")":
                    bal -= 1
            if len(buf)>0:
                buf.append(" ")
            buf.append(token)
            if bal == 0:
                ans.append(''.join(buf))
                buf = []
        if len(buf) > 0:
            ans.append(''.join(buf))
            
        return ans