

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        order = 10** (len(n)//2)
        ans = int(n)
        nochange = self.mirror(n)
        larger = self.mirror((ans//order)*order + order + 1)
        smaller = self.mirror((ans//order)*order - 1)
        if nochange> ans:
            larger = min(nochange,larger)
        elif nochange < ans:
            smaller = max(nochange,smaller)
        
        return str(smaller) if ans-smaller <= larger-ans else str(larger)
        print(nochange,order)
        
        
    def mirror(self,num):
        tmp =[x for x in str(num)]
        i,j = 0,len(tmp)-1
        while i<j:
            tmp[j] = tmp[i]
            i += 1
            j -= 1
        
        return int(''.join(tmp))