# MEDIUM 
# input => [3,2,4,1]
#     Max index,  boundary index
#     2           4
#                     1st [4, 2, 3, 1]
#                     2 [1, 3, 2, 4]
#     1           3
#                     1st [3, 1, 2, 4]
#                     2 [2, 1, 3, 4]
#     0           2
#                     1st [2, 1, 3, 4]
#                     2 [1, 2, 3, 4]

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def findMax(index):
            large = 0
            for i in range(0,index):
                if A[i]>A[large]:
                    large = i
                    
                
            return large
        
        def flip(end):
            start = 0
            while start < end:
                A[start],A[end] = A[end],A[start]
                start += 1
                end -= 1
                
        n = len(A)
        curr = n 
        result = []
        while curr>1:
            large = findMax(curr)
            if large != curr:
                print(large,curr)
                flip(large)
                result.append(large+1)
                print('1st',A)
                flip(curr - 1)
                result.append(curr)
                print("2", A)
            curr -= 1
            
        return result
            
        