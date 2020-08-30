# HARD
# Build a Trie 
#     ex. input [ ["o","a","o","n"],
#                 ["e","t","a","e"],
#                 ["i","h","k","r"],
#                 ["i","f","l","v"]]
#                                         ["oath","oapea","eat","rain"]

#         trie :{'o': {
#                     'a': {
#                         't': {'h': {'$': 'oath'}}, 
#                         'p': {'e': {'a': {'$': 'oapea'}}}
#                         }}, 
#                 'e': {
#                     'a': {
#                         't': {'$': 'eat'}}}, 
#                 'r': {
#                     'a': {
#                         'i': {
#                             'n': {'$': 'rain'}}}}}

#         dfs through every first possible letter and find the rest from four directions

# Time O(row*col * 4*3^length)  Space O(row*col)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
                
            
            node["$"] = word
        row = len(board)
        col = len(board[0])
        result = []
        for i in range(row):
            for j in range(col):
                if  board[i][j] in trie:
                    print(i,j,board[i][j])
                    self.dfs(i,j,trie,board,result)
                    
        return result
        
        
    def dfs(self,i,j,trie,board,result):
        char = board[i][j]
        curr = trie[char]
        match = curr.pop('$',False)
        if match:
            result.append(match)
        board[i][j] = "#" 
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            if self.isValid(i+x,j+y,curr,board):
                self.dfs(i+x,j+y,curr,board,result)
        board[i][j] = char
        if not curr:
            trie.pop(char)
                
    def isValid(self,i,j,trie,board):
        row = len(board)
        col = len(board[0])
        return 0<=i< row and 0<=j<col and board[i][j] in trie
            
            
            
        