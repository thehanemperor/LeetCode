class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
        
        while num >=10:
            tmp = str(num)
            add = 0
            for t in tmp:
                add += int(t)
            num = add
            
        return num