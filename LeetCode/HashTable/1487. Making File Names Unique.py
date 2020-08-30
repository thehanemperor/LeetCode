# MEDIUM

# store every element in a dict with index. if the same appears, increment index 
# ex: ["gta","gta(1)","gta(1)","avalon"]
# appear: {'gta': 0, 'gta(1)': 1, 'gta(1)(1)': 0, 'avalon': 0}

# Time O(N) Space O(N)

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        self.appear = {}
        suffix = [''] *len(names)
        for i in range(len(names)):
            suffix[i] = self.makeFile(names[i])
        return suffix
        
    def makeFile(self,name):
        suffix = name
        index = self.appear.get(suffix,0)
        while suffix in self.appear:
            index +=1
            suffix = name+"({})".format(index)
            
        self.appear[name] = index
        self.appear[suffix] = 0
        return suffix