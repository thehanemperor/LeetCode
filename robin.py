from heapq import heappush,heappop
# matrix rotate, gravity
def gravity(matrix):
    
    print('before')
    m,n = len(matrix),len(matrix[0])
    for ma in matrix:
        print(ma)
    
    rotate = list(map(lambda x: list(x), zip(*(reversed(matrix)))) )
    # rotate = [[0 for _ in range(m)]for _ in range(n)]
    
    # for i in range(n):
    #     for j in range(m):
    #         rotate[i][j] = matrix[j][i]
    #     rotate[i].reverse()

    print('after')
    for r in rotate:
        print(r)
    
class Node():
    def __init__(self,val,left=None,right=None):
        self.left = left
        self.right = right
        self.val = val
def deleteMinimumPeak(nums):
    def isPeak(node):
        #print('is peak',node.val,node.left)
        return node.val!=-1 and node.left.val < node.val and  node.val > node.right.val
    heap = []
    result = []
    nums.append(Node(-1))
    nodes = [Node(val=nums[0],left=Node(val=-1))]
    
    for i in range(1,len(nums)-1):
        curr = Node(val=nums[i],left=nodes[i-1])
        nodes[i-1].right = curr
        if isPeak(nodes[i-1]):
            heappush(heap,(nums[i-1],nodes[i-1]))
        nodes.append(curr)
    
    nodes[i].right = Node(val=-1)
    if isPeak(nodes[i]):
        heappush(heap,(nums[i],nodes[i]))
    for n in nodes:
        print(n.left.val,n.val,n.right.val)
    while heap:
        curr = heappop(heap)
        result.append(curr[0])
        curr[1].right.left = curr[1].left
        curr[1].left.right = curr[1].right
        if  isPeak(curr[1].left):
            heappush(heap,(curr[1].left.val,curr[1].left))
        if isPeak(curr[1].right):
            heappush(heap,(curr[1].right.val,curr[1].right))
        
    print(result)

    
   




    

if __name__ == "__main__":
    a= "...##.....*#."
    b = "...####......"
    # print(len(a),len(b))
    graMatrix = []
    graMatrix.append([x for x in a])
    graMatrix.append([x for x in b])
    # print('range',range(8),type(range(8)))
    # a = list(map(lambda _: [0]*8 ,range(8)))
    # print(a)
    # gravity(graMatrix)

    miniPeak = [2,7,8,5,1,6,3,9,4]
    miniPeak = [3,5,4,9,1]
    
    deleteMinimumPeak(miniPeak)