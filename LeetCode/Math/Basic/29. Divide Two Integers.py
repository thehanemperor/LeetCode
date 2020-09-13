# MEDIUM
# TLE if decrement divisor only 

# Bit manipulation.
#     input: 100 / 3 

#     times = 0
#         3 << 0 = 3
#         3 << 1 = 6
#         3 << 2 = 12
#         3 << 3 = 24
#         3 << 4 = 48
#         3 << 5 = 96
#         3 << 6 = 192 => greater than dividend 100 => stop here 
#     times -=1 because 3 << 6 is too big 
#     result += 1 << times => divided by 32 
#     set dividend to dividend -= divisor << times 

# times O(log N) Space O(1)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        if dividend == 0:
            return 0
        sign = dividend>=0 and divisor>=0 or (dividend<0 and divisor<0)
        left,right = abs(dividend),abs(divisor)
        result = 0
        while left>= right:
            count = 0
            while left >= right<< count:
            
                count += 1
            
            #print('count',count)
            # count -1 because right * count > left
            result += 1 << (count-1)
            #print("result",result)
            left -= right << (count-1)
            #print("dividend",left)
        
        return result if sign else -result   
        
        