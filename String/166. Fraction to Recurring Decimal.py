# MEDIUM 
# Long division 
# Input ==> x, y  output  x/y 
#     1. x % y == 0 ==>  x// y  (Easy Case)
#     2. remainder = x % y 
#         ex.   
#              __0.16__
#            6| 1.00
#               0 ___ 
#               10
#               _6__
#                40
#                36 __
#                 4   <== in the set() so we break here 

# Time O(N) Space O(N)


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        if numerator * denominator <0:
            result.append("-")
            
        divd = abs(numerator)
        divisor = abs(denominator)
        result.append(str(divd // divisor))
        remainder = divd % divisor
        if remainder == 0:
            return ''.join(result)
        
        result.append(".")
        check = {}
        while remainder != 0:
            if remainder in check:
                result.insert(check[remainder],"(")
                result.append(")")
                break
            
            check[remainder] = len(result)
            remainder *=10
            result.append(str(remainder//divisor))
            remainder %= divisor
            
        return ''.join(result)
            