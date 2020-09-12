class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = True
        while i < len(s):
            if s[i]!= " ":
                if s[i] in "+-":
                    sign = False if s[i]== "-" else True
                    i+= 1
                elif not s[i].isdigit():
                    return 0
                break
            i += 1
            
        num = ""
        while i < len(s) and s[i].isdigit():
            num+= s[i]
            i += 1
        
        if not num:
            return 0
        result = int(num)
        
        if result < 2**31:
            return result if sign else -result
        else:
            return 2**31 -1 if sign else -2**31
                
            