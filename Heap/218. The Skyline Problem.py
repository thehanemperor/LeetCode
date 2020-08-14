class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            xLeft,xRight,y = buildings[0]
            return [[xLeft,y],[xRight,0]]
        
        leftSky = self.getSkyline(buildings[: n//2])
        rightSky = self.getSkyline(buildings[n//2 :])
        print('left',leftSky,'rihgt',rightSky)
        return self.merge(leftSky,rightSky)
    
    def merge(self,left,right):
        
        leftLen = len(left)
        rightLen = len(right)
        pl,pr = 0,0
        currY = leftY = rightY= 0
        result = []
        
        while pl < leftLen and pr < rightLen:
            leftPoint,rightPoint = left[pl],right[pr]
            if leftPoint[0] < rightPoint[0]:
                x,leftY = leftPoint
                pl += 1
                
            else:
                x,rightY = rightPoint
                pr += 1
            
            maxY = max(leftY,rightY)
            if currY != maxY:
                self.update(x,maxY,result)
                currY = maxY
        print('first merge',result)
        self.appendSky(pl,left,leftLen,leftY,currY,result)
        self.appendSky(pr,right,rightLen,rightY,currY,result)
        
        return result
        
    def update(self,x,y,result):
        if not result or result[-1][0] != x:
            result.append([x,y])
            
        else:
            result[-1][1] = y
            
    def appendSky(self,p,num,n,y,currY,result):
        while p <n:
            x,y = num[p]
            p+=1
            if currY != y:
                self.update(x,y,result)
                currY = y
            
