# HARD 

# 1. check length + counts of word + current word with maxWidth
# 2. round robin 
#     maxWidth - lenght = number of spaces
#     loop through number of spaces times
#         each time assign a space to a word[0] -word[len]

# Time O(N)  Space O(N)

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        length = 0
        result = []
        for word in words:
            if length+ len(line) +len(word) > maxWidth:
                
                for i in range(maxWidth - length):
                    line[i % (len(line)-1  or 1)]+=" "
                
                result.append("".join(line))
                length = 0
                line = []
            
            line.append(word)
            length+= len(word)
            
        result.append(" ".join(line).ljust(maxWidth))
        return result