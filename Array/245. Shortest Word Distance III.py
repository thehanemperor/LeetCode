# Medium 
# same as 243, but we add each index of word into a dict{}
# 1. if word1 == word2, we compare every pair of dict[word1] and find the min 
# 2. same as 243M
# time Worst O(N^2)  Space O(N)


def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        pos = defaultdict(list)
        for i,v in enumerate(words):
            pos[v].append(i)
            
        gmin = float("inf")
        if word1 == word2:
            for i in range(1,len(pos[word1])):
                gmin = min(gmin,pos[word1][i]-pos[word1][i-1])
            return gmin
        for i in pos[word1]:
            for j in pos[word2]:
                gmin = min(gmin,abs(i-j))
                
        return gmin
