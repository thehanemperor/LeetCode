class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        print('length',len(s))
        check = {}
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            check[tmp] = check.get(tmp,0)+1
            if check[tmp] == 2:
                result.append(tmp)
            
        
        return result