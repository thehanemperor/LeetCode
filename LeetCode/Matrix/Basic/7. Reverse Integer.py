class Solution:
    def reverse(self, x: int) -> int:
        if -10< x< 10:
            return x
        
        
        sign = x>0
        result = int(str(abs(x))[::-1])
        if result> 2**31:
            return 0
        
        return result if sign else 0-result