# MEDIUM 
# inplace => bits operation

# scan 3 top/down/left/right + itself = 9 elements total and each of em & 1
# if number of  & 1 == 3 or number of & 1 - board[i][j] == 3, we got live element 

# finally each cell >> 1 and we have the result 

# Time O(N)  Space O(1)


def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    neighbors = [0,1,-1]
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            lives = 0
            for y in range(max(0,i-1),min(row,i+2)):
                for x in range(max(0,j-1),min(col,j+2)):
                    lives += board[y][x] & 1
            #print([i,j],lives)    
            if lives == 3 or lives- board[i][j] ==3:
                board[i][j] |= 2
                
        print(board[i])
                
    for i in range(row):
        for j in range(col):
            board[i][j]>>=1
            
    