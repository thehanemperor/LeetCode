# MEDIUM
# find smallest x, largest x, draw a line to split those two value 
# store all points in to a set([])
# check if every point in set can be matched by mirroring the y axis 

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        print(max(points),min(points))
        check = set([(x,y) for x,y in points])
        count = 0
        minx,maxx = float("inf"), -float("inf")
        for x,y in points:
            minx = min(minx,x)
            maxx = max(maxx,x)
        
        line = (maxx+ minx) / 2
        
        for x,y in check:
            diff = abs(x-line)
            
            if x > line:
                if (x-diff*2,y) not in check:
                    return False
            elif x< line:
                if (x+diff*2,y) not in check :
                    return False
            
        return True
