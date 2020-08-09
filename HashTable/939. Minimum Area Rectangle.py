# MEDIUM 
# two points can form a rectangle, 两个对角线的端点 
# save all points in set()
# check every two pairs of points, points[i],points[j] as two diagnal points 
# calculate the area of this rectangle

# Time O(N^2) Space O(N)

def diagnal(self,points):
        appear = set([(x,y) for x,y in points])
        #print(appear)
        n = len(points)
        result = float("inf")
        for i in range(n):
            for j in range(i):
                p1 = (points[j][0],points[i][1])
                p2 = (points[i][0] ,points[j][1])
                #print(points[i],points[j], p1,p2)
                if points[i][0]!= points[j][0] and points[i][1] != points[j][1] \
                    and p1 in appear and p2 in appear:
                    result = min(result,
                                 abs(points[i][0] - points[j][0]) *
                                 abs(points[i][1] - points[j][1])
                                )
        return result if result != float('inf') else 0