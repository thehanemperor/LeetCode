# HARD 

# 1. find prefix sum of a matrix 
#     prefix[i-1][j] +prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1]
#     ex. prefix matrix=> 
#                         [0, 1, 1]
#                         [1, 3, 4]
#                         [1, 4, ?]  find the ? value, we add uppper? and left of ?, and - overlapped area prefix[i-1][j-1]

# 2. loop row^2 and col to find every possible sum 

# Time O(row^2*col) Space O(row*col)


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row= len(matrix)
        col = len(matrix[0])
        prefix =[[0 for _ in range(col+1)] for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                prefix[i][j] = prefix[i-1][j] +prefix[i][j-1] - \
                            prefix[i-1][j-1] + matrix[i-1][j-1]
           
        
        result = 0
        for r1 in range(1,row+1):
            for r2 in range(r1,row+1):
                count = {}
                count[0]= 1
                for c in range(1,col+1):
                    
                    curr = prefix[r2][c] - prefix[r1-1][c]
                    #print('r1:{} r2:{} c:{} curr:{}'.format(r1-1,r2,c,curr))
                    result += count.get(curr -target,0)
                    count[curr] = count.get(curr,0)+1
                    
                    
        return result