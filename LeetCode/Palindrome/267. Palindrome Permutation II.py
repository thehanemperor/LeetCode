# MEDIUM
# since this is looking for permutation, the Time would be O(N!)
# 1. first check if the input can form a palindrome => only <=1 odd occured char can used 
# 2. only permutate the half of the input == permutation II
#    eg. input = "aabb"
#         only permutate ["a","b"], append reversed(input) to the end 

# Time O(N/2 !) Space O(N)
    

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        check = [0]* 128
        half = [0]* (len(s)//2)
        if not self.canPalin(s,check):
            return []
        k = 0
        ch =0
        for i in range(128):
            if check[i]%2== 1:
                ch = chr(i)
            for j in range(check[i]//2):
                half[k] = chr(i)
                k +=1
        
        print(ch)
        print(half)
        result = set([])
        self.dfs(half,0,ch,result)
        return list(result)
        
    def dfs(self,half,index,ch,result):
        if index == len(half):
            if ch:
                result.add("".join(half) + ch + "".join(reversed(half)) )
            else:
                result.add("".join(half) + "".join(reversed(half)) )
            return 
        check = set([])
        for i in range(index,len(half)):
            if half[i] not in check:
                check.add(half[i])
                half[i],half[index] = half[index],half[i]
                self.dfs(half,index+1,ch,result)
                half[i],half[index] = half[index],half[i]
            
    def isPalin(self,s):
        i,j = 0,len(s)-1
        while i<j:
            if s[i]!= s[j]:
                return False
            i+= 1
            j -= 1
            
        return True
            
    def canPalin(self,s,check):
        count = 0
        for i in range(len(s)):
            t = ord(s[i])
            check[t] += 1
            if check[t] %2 == 0:
                count -= 1
            else:
                count += 1
                
        return count <= 1
            