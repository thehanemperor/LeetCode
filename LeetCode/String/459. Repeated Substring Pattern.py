# EASY 
# KMP 
# only build prefix 
# ex.  input = ababa
#     prefix[0] = 0 
#     prefix[1] = 0    
#     prefix[2] = 1   a,b,a 
#     prefix[3] = 2   ab ab 
#     prefix[4] = 3   aba  aba 


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def buildPrefix():
            n = len(s)
            prefix = [0]*len(s)
            length = 0
            i = 1
            while i < len(s):
                if s[i] == s[length]:
                    
                    length += 1
                    prefix[i] = length
                    i += 1
                    
                else:
                    if length >0:
                        
                        length = prefix[length -1]
                    else:
                        prefix[i] = length
                        i += 1
            print(prefix)
            l = prefix[n-1]
            return l!= 0 and n %(n- l) == 0
        return buildPrefix()