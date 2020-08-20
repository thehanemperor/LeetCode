"""
1. 求平均数和众数，保留4位小数
2. 数组长度
3. Maxdiff， C++同样11/14 有3个test case过不去

"""

"""
Word Search Problem : Write a Python or Java Program

You are given a grid of n*n letters, followed by m number of words. The words may occur anywhere in the grid in a row or a column, forward or backward. There are no diagonal words, however.

Print space separated strings "Yes" if the word is present and "No" if it isn't.

Example 0:

Input:

3

C A T

I D O

M O M

5

CAT TOM ADO MOM CDM

OUTPUT:

Yes Yes Yes Yes No

Input 1:

3

M O M

S O N

R A T

4

MNT MSR OOB

OUTPUT:

Yes Yes No
"""

def wordSearch(matrix,words):
    row = len(matrix)
    col = len(matrix[0])
    dict_t = {}
    for word in words:
        tmp = dict_t
        for char in word:
            if char not in tmp:
                tmp[char]= {}
            tmp = tmp[char]
        tmp["$"] = word
    result = []
    

    directions = {"up":(-1,0),
                    "down":(1,0),
                    "left":(0,-1),
                    "right":(0,1)
                    }    
    def dfs(index,direc,root,i,j):
        tmp =matrix[i][j]
        child = root[matrix[i][j]]
        matrix[i][j] = "#"
        
        if "$" in child:
            result.append(child["$"])
            child.pop("$")

        if not direc:
            for k,v in directions.items():
                x,y = v 
                
                if isValid(i+x,j+y,child):
                    #print('dfs',matrix[i+x][j+y],child)
                    dfs(index,k,child,i+x,j+y)

        else:
            x,y = directions[direc]
            if isValid(i+x,j+y,child):
                dfs(index,direc,child,i+x,j+y)
        matrix[i][j] = tmp


    def isValid(i,j,child):
        
        return 0<=i<row and 0<=j<col and matrix[i][j] in child


    for i in range(row):
        for j in range(col):
            if matrix[i][j] in dict_t:
                dfs(0,False,dict_t,i,j)
                
    print(result)


class LCMaxSubArray:
    def maxSubArray(self, nums) -> int:
            gmax = nums[0]
            prev = nums[0]
            for i in range(1,len(nums)):
                if prev <0:
                    curr = nums[i]
                else:
                    curr = nums[i]+ prev
                gmax = max(gmax,curr)
                prev = curr
                
            return gmax
            
            
    def dpv(self,nums):
        dp = [0]* len(nums)
        dp[0] = nums[0]
        gmax = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1]<0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i] 
            
            gmax = max(gmax,dp[i])
            
        return gmax

# primes:
def findPrimeON(arr):
    gmax = max(arr)
    prime=[]
    SPF= [None]* (gmax+1)
    isPrime= [True]*(gmax+1)
    for i in range(2,gmax+1):
        if isPrime[i] == True:
           prime.append(i)
           SPF[i] = i
        j = 0
        while j < len(prime) and i* prime[j]<gmax and prime[j]<= SPF[i]:
            isPrime[i*prime[j]]= False
            SPF[i* prime[j]] =prime[j]
            j+= 1
    print(prime)


def findPrime(arr):
    gmax = max(arr)
    primes=[True]* gmax
    for i in range(2,gmax):
        j = 2
        while j<gmax and i*j < gmax:
            primes[i*j] = False  
            j+= 1

def modeMean(nums):
    count = [0]*(max(nums)+1)
    total = 0
    mode = 0
    for i in nums:
        count[i] += 1
        total += i
        if count[i] == mode:
            if i < mode:
                mode = i
        if count[i]>mode:
            mode = i
    avg = total/len(nums)
    print("{:.4f} {}".format(avg,mode))

def nJar(nums):
    dp =[-float(inf)]* (len(nums)+1)
    dp[0] = 0
    dp[1] = max(0,nums[0])
    
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])

    #print(max(max(dp[])))

def countSetBits(n):
    count = 0
    while n:
        n &= (n-1)
        count += 1
    print(count)

def decodeString(s):
    #(ab(d){3}){2}
    
    sym = {"}":"{", ")":"(" }
    string = num = ""
    stack = []
    for char in s:
        if char == "}":
            prefix = stack.pop()
            string = prefix + int(num)* string
        elif char.isdigit():
            num += char
        elif char == "{":
            num = ""
        elif char == "(":
            stack.append(string)
            string = ""
        elif char == ")":
            pass
        elif char.isalpha():
            string += char

    print(string)

def decodeWay(s):
    dp = [0]* (len(s)+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(1,len(s)):
        if 10<=int(s[i-1]+s[i])<=25:
            dp[i+1] = dp[i-1]+dp[i]
        else:
            dp[i+1] = dp[i]
    
    print(dp[-1])

def queenAttack(qx, qy, ox, oy):
    if qx == ox:
        return True
    
    if qy == oy:
        return True
    
    if abs(qx-ox) == abs(qy-oy):
        return True
    
    return False

def rotateImageNXN(matrix):
   
        
    def dfs(index, matrix, row):
        if row <1:
            return
        
        for i in range(row-1):
            first = matrix[index][i+index]
            matrix[index][i+index] = matrix[index+row-1-i][index]
            matrix[index+row-1-i][index] = matrix[row-1+index][row-1+index-i]
            matrix[row-1+index][row-1+index-i] = matrix[index+i][row-1+index]
            matrix[index+i][row-1+index] = first
            
        dfs(index+1,matrix,row-2)
    dfs(0,matrix,len(matrix))

def rotateImageMN(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] =matrix[j][i]

    for r in result:
        print(r)
    print("==========")
    for i in range(n):
        result[i].reverse()

    for r in result:
        print(r)

def maxDiff(arr, arr_size): 
    max_diff = arr[1] - arr[0] 
    min_element = arr[0] 
      
    for i in range( 1, arr_size ): 
        if (arr[i] - min_element > max_diff): 
            max_diff = arr[i] - min_element 
      
        if (arr[i] < min_element): 
            min_element = arr[i] 
    return max_diff 

def validIPAddress(IP) :

    def validate_IPv4( IP) -> str:
        nums = IP.split('.')
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"
    
    def validate_IPv6( IP) :
        nums = IP.split(':')
        
        hexdigits = '0123456789abcdefABCDEF'
        
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"

    if IP.count('.') == 3:
        return validate_IPv4(IP)
    elif IP.count(':') == 7:
        return validate_IPv6(IP)
    else:
        return "Neither"


if __name__ == "__main__":
    #modeMean([1,2,7,3,2,7,7,7,7,7,7,2,2,2,2,2])
    #decodeString("(ab(d){3}){2}")    
    # output=> abdddabddd

    #decodeWay("100200300")

    matrixMN = []
    c = 1
    for i in range(4):
        matrixMN.append([j for j in range(c,c+3)])
        c+=3

    # Driver program to test above function  
    arr = [1, 2, 6, 80, 100] 
    size = len(arr) 
    
    board = [
        ['C', 'A', 'T'],
        ['I', 'D', 'O'],
        ['M', 'O', 'M'],]



    words = [ 'CAT', 'TOM', 'ADO', 'MOM', 'CDM',]
    wordSearch(board,words)
    # OUTPUT:

    # Yes Yes Yes Yes No
 
    #maxDiff(arr, size)
    #countSetBits(10)
    print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    
    #rotateImageMN(matrixMN)

    #findPrimeON([188])