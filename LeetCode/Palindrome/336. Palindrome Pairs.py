# HARD
# input ["abcd","dcba","lls","s","sssll"]


# scan each word of the input and store {word:index} into a dict:
#     1. check if the reversed(word) also in dict and the index is not same 
#     2. check suffix of a word 
#         eg. word = "lls"
#             "l" is palindromic => check reversed("ls") in dict
#             "ll" is palindromic => check reversed("s") in dict => True 
#     3. check prefix of a word 
    
# Time O(K^2 * N) Space O(N)


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        check = {}
        result = []
        for i,v in enumerate(words):
            check[v] = i
            
        for k,v in check.items():
            rever = ''.join(list(reversed(k)))
            if rever in check and check[rever]!=v:
                result.append([v,check[rever]])
                
            
            """
                check suffix
                word = abac
                1. *cab* a "bac"
                2. *c* aba "c"
            """
            for suffix in self.validSuffix(k):
                #print(suffix)
                if suffix in check:
                    result.append([check[suffix],v])
                    
            for prefix in self.validPrefix(k):
                #print(prefix)
                if prefix in check:
                    result.append([v,check[prefix]])
                    
        return result
                
            
            
    def validSuffix(self,word):
        suffix = []
        for i in range(len(word)):
            if self.isPalin(word,0,i):
                suffix.append(''.join(reversed(list(word[i+1:]))) )
                
        return suffix
    
    def validPrefix(self,word):
        prefix = []
        n = len(word)
        for i in range(n):
            if self.isPalin(word,i,n-1):
                prefix.append( ''.join(reversed(list(word[:i]))) )
        return prefix
            
    
    def isPalin(self,word,i,j):
        while i<j:
            if word[i]!= word[j]:
                return False
            i+= 1
            j -= 1
            
        return True