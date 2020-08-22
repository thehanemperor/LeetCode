from heapq import heappush,heappop
from collections import deque
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

def restoreOrder(matrix):
    indegree = {}
    graph = {}
    for after,b4 in matrix:
        indegree[after] = indegree.get(after,0)+1
        indegree[b4] = indegree.get(b4,0)+1
        if b4 not in graph:

            graph[b4]=[after]
        else:
            graph[b4].append(after)

        if after not in graph:
            graph[after] = [b4]
        else:
            graph[after].append(b4)
    
    queue = deque([])
    visited = set([])
    result = []
    for k,v in indegree.items():
        if v == 1:
            node = k
            visited.add(k)
            break

    def dfs(curr):
        
        visited.add(curr)
        result.append(curr)
        for nei in graph[curr]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)

    dfs(node)    
    #print('in',indegree,"graph",graph)
    
    print(result)

def textEditor(operations):
    def undo(lastOP,lastString,result):
        if not lastOp:
            return result
        op = lastOp.pop()
        part = lastString.pop()
        length = len(result)
        if op == "INSERT":
            result = result[:length-len(part)]
        elif op == "PASTE":
            result = result[:length-len(part)]
        elif op == "DELETE":
            result += part
        
        return result

    result = ""
    lastCopied = ""
    lastPasted = ""
    lastDelete = ""
    lastInsert = ""
    lastOp = []
    lastString = []

    for op in operations:
        curr = op.split(" ")
        if curr[0] == "INSERT" and len(curr)==2:
            
            lastInsert = curr[1]
            result += lastInsert
            lastOp.append(curr[0])
            lastString.append(lastInsert)
        elif curr[0] == "DELETE":
            if not result:
                continue
            lastDelete = result[-1]
            result = result[:-1]
            lastOp.append(curr[0])
            lastString.append(lastDelete)
        elif curr[0] =="UNDO":
            result = undo(lastOp,lastString,result)
        elif curr[0] == "COPY":
            lastCopied = result[int(curr[1]):]
        elif curr[0] == "PASTE":
            if lastCopied:
                lastPasted = lastCopied
                result += lastPasted
                lastOp.append(curr[0])
                lastString.append(lastPasted)

    print(result)


def coolFeature(a,b,query):
    def sum2(a,b,x):
        result = 0
        check = {}
        for i in a:
            check[x-i] = check.get(x-i,0)+1
        for i in b:
            if i in check:
                result += check[i]
        print('2sum',a,b,x,'result',result)
        return result

    result = []
    for q in query:
        if len(q) == 3 and q[0] == 0:
            b[q[0]] = q[2]
        elif len(q) == 2 and q[0] == 1:
            result.append(sum2(a,b,q[1]))
    
    print('coolfeature',result)
    return result



    

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
    topoPair = [[1,2],[4,2],[1,5],[3,5]]
    topoPair = [[2,1],[2,3],[3,4]]
    operations = ["INSERT Code","INSERT Signal","DELETE","UNDO"]
    operations = ["INSERT Da","COPY 0","UNDO","PASTE","PASTE","COPY 2","PASTE","PASTE","DELETE","INSERT aaam"]
    operations = ["INSERT a","DELETE","COPY 0","UNDO","PASTE","UNDO","INSERT b","COPY 0","PASTE","COPY 2","PASTE","UNDO",
                    "DELETE","UNDO"]
    coola=[1,2,2]
    coolb=[2,3]
    coolq=[[1,4],[0,0,3],[1,5]]
    coolFeature(coola,coolb,coolq)
    #textEditor(operations)
    #restoreOrder(topoPair)

    #deleteMinimumPeak(miniPeak)