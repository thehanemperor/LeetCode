# MEDIUM
# same as 243, but the words have duplicated value
# add index of each word to a dict{list}
# compare each pair of dict[word1] and dict[word2]

# time Worst O(N^2)  Space O(N)

class WordDistance:

    def __init__(self, words: List[str]):
        self.pos = defaultdict(list)
        for i,v in enumerate(words):
            self.pos[v].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        gmin = float("inf")
        for i in self.pos[word1]:
            for j in self.pos[word2]:
                gmin = min(gmin,abs(i-j))
                
        return gmin
