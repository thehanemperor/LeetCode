class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        return self.iterative(x,n)
        if n >0:
            
            return self.dfs(x,n)
        if n< 0:
            return 1 / self.dfs(x,abs(n))
        
    def iterative(self,x,n):
        count = abs(n)
        ans = 1
        result = x if n>0 else 1/x
        while count > 0:
            if count%2 !=0:
                ans *= result
            result *= result
            count //=2
        return ans
        
    def dfs(self,x,n):
        
        if n == 2:
            return x*x
        if n == 1:
            return x
        
        tmp = self.dfs(x,n//2)
        
        if n%2 == 0:
            
            return tmp *tmp
        if n%2 == 1:
    
            return tmp * tmp * x
            
            
    