# HARD
# since we want to find the combined length of [words], means => loop through s[0:len(s)-len(words)]
# two loops.
#     1. first loop is to check an element as a start of a potential result 
#     2. second loop is to check if s[i:i+len(words)] a correct substring 

# Time O(N^2)  Space O(N)

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        
        result = []
        n = len(words)
        m = len(words[0])
        count = Counter(words)
        # print('count',count)
        for i in range(len(s)- n*m+1):
            check = {}
            j = i
            flag = 0
            
            while j < n*m+j:
                
                t = s[j:j+m]
                # print(i,t)
                if t not in count:
                    break
                check[t] = check.get(t,0)+ 1
                if check[t]> count[t]:
                    
                    break
                flag += 1
                j += m
                
            
            if flag==n:
                result.append(i)
                
        return result