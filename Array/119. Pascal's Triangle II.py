# EASY 
# rolling array

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        result = [0]* (rowIndex +1)
        result[0],result[1] = 1,1
        for i in range(2,rowIndex +1):
            prev = result[0]
            for j in range(1,i+1):
                
                curr = result[j]
                result[j] += prev
                prev = curr
            result[j] = 1
        
        return result
        