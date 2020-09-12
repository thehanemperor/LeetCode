class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = deque([])
        if len(b)>len(a):
            a,b = b,a 
        alen,blen = len(a),len(b)
        i= 0
        
        while i < blen:
            tmp = int(a[alen-1-i]) + int(b[blen-1-i])+carry
            carry = 0
            if tmp >=2:
                carry = 1
                
            result.appendleft(str(tmp%2))
            i += 1
            
        while i < alen:
            tmp = int(a[alen-1-i])+ carry
            carry = 0
            if tmp >=2:
                carry = 1
                
            result.appendleft(str(tmp%2))
            i += 1
        
        if carry:
            result.appendleft("1")
            
        return ''.join(result)
            