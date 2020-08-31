# HARD 
# store all possible a&b into an Array as count
# a:2, b:2, a&b: 2  ==> count[2]+1
# a:2, b:1, a&b: 0
# a:2, b:3, a&b: 2
# a:1, b:2, a&b: 0
# a:1, b:1, a&b: 1
# a:1, b:3, a&b: 1
# a:3, b:2, a&b: 2
# a:3, b:1, a&b: 1
# a:3, b:3, a&b: 3

# nested for loop with (a in A)
#         i in range(n+1)
#         if a&i in array, result + count[a&i]

class Solution:
   
    def countTriplets(self, A: List[int]) -> int:
        n = max(A)
        count =[0]*(n+1)
        for a in A:
            for b in A:
                
                count[a&b] += 1
        
        result = 0
        for a in A:
            for i in range(n+1):
                if a & i == 0:
                    result += count[i]
                    
        return result
