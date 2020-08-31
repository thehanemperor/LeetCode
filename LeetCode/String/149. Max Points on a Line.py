# HARD 
# loop through every pair of points and find the slope 
# slope represented with fraction ==>  x/y.
# since we need unique fractions, we need find the Greatest Common divisor of two numbers

# Time O(N^2) Space O(N)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        for i in range(n):
            count = {}
            same = 1
            currMax = 0
            for j in range(i+1,n):
                p1 = points[i]
                p2 = points[j]
                if p1 == p2:
                    same += 1
                else:
                    slope = self.getSlope(p1,p2)
                    if slope in count:
                        count[slope]+=1
                    else:
                        count[slope] = 1 
                    currMax = max(currMax,count[slope])
            result = max(result,same+ currMax)
        return result 


    def getSlope(self,p1,p2):
        dx = p2[0]-p1[0]
        dy = p2[1] - p1[1]
        if dx == 0:
            return (0,p1[1])
        if dy == 0:
            return (p1[0], 0)
        cd = self.gcd(dx,dy)
        return (dx//cd, dy //cd )
        
    def gcd(self,x,y):
        return x if y == 0 else self.gcd(y, x % y)
