from heapq import heappush,heappop
from collections import deque
import random
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

def justifyNewpaper(lines,align,width):
    result = ["*"*(width+2)]
    for i in range(len(lines)):
        curr = []
        length = 0
        
        for word in lines[i]:
            
            if len(word)+ length + len(curr)-1 >width:
                if align[i] == "LEFT":
                    result.append("*"+' '.join(curr).ljust(width)+"*")
                else:
                    result.append("*"+' '.join(curr).rjust(width)+"*")
                curr = []
                length = 0
            curr.append(word)
            length += len(word)
        
        #print(curr,align[i])
        if align[i] == "LEFT":
            #print('left,curr',curr)
            result.append("*" +' '.join(curr).ljust(width)+"*")
        else:
            result.append("*"+' '.join(curr).rjust(width)+"*")
    result.append("*"*(width+2))   
    for r in result:
        print(r)

def kOccurence(sequence,words):
    # sliding window
    result = []
    for word in words:
        
        start,end = 0,0
        k = 0
        gmax = 0
        count = 0
        while end < len(sequence):
            if sequence[end] ==word[k]:
                #print(sequence[end])
                end += 1
                k += 1
                if k == len(word):
                    k = 0
                    count += 1
                    gmax = max(gmax,count)
            else:
                count = 0
                k = 0 if word[0]!= sequence[end] else 1
                end += 1
            
        result.append(gmax)
            
    print(result)

def pairSum2(array):
    power = []
    for i in range(32):
        power.append(2**i)
    result = 0
    print(array)
    for p in power:
        check = set([])
        for num in array:
            check.add(p-num)
            if num in check:
                result += 1
            
                print(p-num,num,p)
            
    print(result)
    
def gotoMall(n,m,x1,y1,x2,y2):
    matrix = list(map(lambda x: [0]*m ,range(n)))
    print('start',y1,x1,'end',y2,x2)
    for ma in matrix:
        print(ma)
    i,j = y1,x1
    destX,destY = y2,x2
    def isValid(x,y,direc):
        rev ={
            -1 : 1,
            1 : -1
        }
        
        if (x + direc[0] <0 or x+direc[0] >=n) and ( y+direc[1] <0 or y+direc[1]>=m ):
            return [rev[direc[0]],rev[direc[1]]]
        elif x+direc[0] <0 or x+direc[0] >=n :
            return [rev[direc[0]],direc[1]]
        elif y+direc[1] <0 or y+direc[1]>=m :
            return [direc[0], rev[direc[1]]]
        
        return direc
    direc = [-1,1]
    went = {}
    count = 0
    while not (i== destX and j == destY):
        
        # -1, 1
        
        if matrix[i][j] == 3:
            break
        matrix[i][j] +=1
        print(i,j,'step',count)
        for ma in matrix:
            print(ma)
        direc = isValid(i,j,direc) 
        i += direc[0]
        j += direc[1]
        #print('next',i,j,direc)
        count +=1 
    
    if i==destX and j == destY:
        print(True,i,j,"step",count)
    else:
        print(False,i,j,"step",count)
    
from collections import defaultdict
def revPair(array):
    check = defaultdict(list)
    for a in array:
        tmp =str(a) 
    """
    hashmap {
        a-rev(a)
        0: [a...]
        1: [a...]
    }
    every key find combination 2
    """

def countSplitArray(array):
    n = len(array)
    prefix = [0]*n
    sufix = [0]*n
    
    count = 0
    for i in range(n):
        count += array[i]
        prefix[i] = count
    
    count = 0
    for i in range(n-1,-1,-1):
        count+= array[i]
        sufix[i] = count
    print(array)
    print(prefix)
    print(sufix)
    s,e = 1,1
    currSubArrSum, count = 0,0
    while s < n-1 and e <n-1:
        while e < n-1 and currSubArrSum < prefix[s-1]:
            currSubArrSum+= array[e]
            e+= 1
        if currSubArrSum <= sufix[e]:
            count += 1
        
        currSubArrSum -= array[s]
        s += 1
    print(count)
#def sawTooth(array):


    

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
    #coolFeature(coola,coolb,coolq)
    #textEditor(operations)
    #restoreOrder(topoPair)
    lines = [["hello", "world","la","jfiwng","jfienguj"],["how","areYou","doing"],["Please look","and align", "to right"]]
    aligns = ["LEFT","RIGHT","RIGHT"]
    width = 16
    #justifyNewpaper(lines,aligns,width)
    sequence = "abcdaaaa"
    words =["ab", "abcd","bca","a"]
    #kOccurence(sequence,words)
    pairPower=[-2,-1,0,1,2]
    mallN = random.randint(5,10)
    mallM = random.randint(5,10)
    #gotoMall(mallN,mallM,random.randint(0,mallM-1),random.randint(0,mallN-1),random.randint(0,mallM-1),random.randint(0,mallN-1))
    split3Array = [1,1,1]
    countSplitArray(split3Array)
    #pairSum2(pairPower)
    #deleteMinimumPeak(miniPeak)