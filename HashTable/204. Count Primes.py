# EASY 
# find all multiples less than n 
#     ex  Input 6
#             arr = [1:True, 2:True ,3:True ,4:True ,5:True ]
#             start from 2, mark 2*2, 2*3, 2*4 ... False 

# Time O(N^2) Space O(N)


class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [1 for _ in range(n)]
        count = 0
        for i in range(2,n):
            j = 2
            
            while arr[i] and i*j < n:
                arr[i*j] = 0
                j += 1
                    
        for i in range(2,n):
            if arr[i]:
                count+= 1
                
        return count
