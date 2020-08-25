# EASY
# i,j represent index of words == word1, word2
# since we are looking for the closest pair we assign new value to each of em and compare with the min 

# time O(N) space O(1)

def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1,i2 = -1,-1
        gmin = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i
                
            if i1 != -1 and i2 != -1:
                gmin = min(gmin,abs(i1-i2))
                
        return gmin