# EASY 
# calculate every pair of the list and count the permutation of the pairs

# Time O(N^2) Space O(N)

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        for i in range(n):
            appear = {}
            p1 = points[i]
            for j in range(n):
                if i==j:
                    continue
                
                p2 = points[j]
                d = self.getDistance(p1,p2) 
                if d not in appear:
                    appear[d] = 1
                else:
                    result += appear[d]
                    appear[d]+=1
                
            
        return result*2
    
    def getDistance(self,p1,p2):
        dx = p2[0]-p1[0]
        dy = p2[1] - p1[1]
        
        return dx**2 + dy**2
        
        