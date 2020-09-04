# MEDIUM

# when n = 1
#     we have ["1","0","8"]
# when n = 2:
#     we have ["11","69","88","96","00"]
# n = 3:
#     we have ["111","101","181","619","609","689","818","808","888","916","906","986"]
#     which is ["1","0","8"] inserted in the mid of ["11","69","88","96","00"]

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        odd = ["1","0","8"]
        even = ["11","69","88","96","00"]
        
        if n == 1:
            return odd
        elif n == 2:
            return even[:-1]
        elif n%2 ==0:
            pre,after = self.findStrobogrammatic(n-2),even
        else:
            pre,after = self.findStrobogrammatic(n-1),odd
            
        premid = (n-1)//2
        tmp = []
        
        for p in pre:
            for c in after:
                tmp.append(p[:premid] + c + p[premid:]) 
                
        return tmp
        