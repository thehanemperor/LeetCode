# MEDIUM

# input: a: 3 b:5  c: 4
#         is it possible get 4 use 3 and 5
#         1. pour water to a, pour water to b from a => a:0 b:3
#         2. pour water to a, pour water to b from a => a:1 b:5 
#         3. pour water out of b, pour water to b from a => a:0 b:1 
#         4. fill a and pour water to b => a:0 b:4 

# if c is multiple of gcd(a,b) => True 

# find gcd => a / b => b * result +  a%b
#     gcd(a,b) = gcd(b, a%b)

# Time O(N) Space O(N)
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x == 0 or y == 0:
            return x== z or y == z
        if x + y < z:
            return False
        common = self.gcd(x,y)
        return z % common == 0
        
    def gcd(self,a,b):
        return a if b == 0 else self.gcd(b,a%b)