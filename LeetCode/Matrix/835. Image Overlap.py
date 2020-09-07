# MEDIUM 

# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]

# shift Right, Down -> compare A to B 

# shift Left, Up -> compare B to A 

# e.g 
# shift left: 1, right: 0, up: 1, Down: 0 

#     compare A[1:end][1:end] with B[:][:]

# shift left: 0, right: 1, up: 0, Down: 1

#     compare B[1:end][1:end] with A[:][:]

# Time O(N^4)  Space O(1)


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        gmax = 0
        for i in range(len(A)):
            for  j in range(len(A)):
                
                gmax = max(gmax,self.shift(j,i,A,B))
                gmax = max(gmax,self.shift(j,i,B,A))
                
            

        return gmax
    
    
   
    def shift(self,colShift,rowShift,change,static):
        count = 0
        
        sRow = 0
        for i in range(rowShift,len(change)):
            cCol = 0
            for j in range(colShift,len(change)):
                if change[i][j] == 1 and change[i][j] ==static[sRow][cCol]:
                    count += 1
                
                cCol += 1
            sRow += 1
            
        return count
        
 