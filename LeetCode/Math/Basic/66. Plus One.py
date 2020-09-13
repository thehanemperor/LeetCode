class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1,-1,-1):
            tmp = digits[i] +carry
            carry = 0
            if tmp>=10:
                
                carry =1
            digits[i] = tmp% 10
            if carry == 0:
                return digits
                
        return [1]+digits
        
            