import random

for i in range(4):

    #arr.append([random.randint(0,10),random.randint(0,10),random.randint(0,10)])

# print(arr)

# arr.sort(key=lambda x: (-x[2],x[1]))

print(arr)

# citadel OA 

#1. throttle gate 

import collections
def droppedRequests(requestTime):
    if len(requestTime) <= 3: return 0
    count = collections.Counter(requestTime)
    lookup = collections.defaultdict(int)
    for i in range(requestTime[0], requestTime[-1]+1):
        lookup[i] = lookup[i-1] + count[i]
    for i in range(3, len(requestTime)):
        temp1 , temp2 = 0, 0
        if requestTime[i]-10 in lookup: temp1 = lookup[requestTime[i]-10]
        if requestTime[i]-60 in lookup: temp2 = lookup[requestTime[i]-60]
        if requestTime[i-3] == requestTime[i]: requestTime[i-3] = '$'
        elif i+1 - temp1 > 20: requestTime[i] = '$'
        elif i+1 - temp2 > 60: requestTime[i] = '$'
    return requestTime.count('$') 

# 2 can make palindrome

def canMakePaliQueries(s, queries):
    N = 26
    a = ord('a')
    dp = [[0] * N]
    for i in range(1, len(s)+1):
        new = dp[i-1][:]
        j = ord(s[i-1]) - a
        new[j] += 1
        dp.append(new)
    ans = []
    for l, r, k in queries:
        L = dp[l]
        R = dp[r+1]
        ans.append(sum((R[i] - L[i]) & 1 for i in range(N)) // 2 <= k)
    return ans
 
# 3. consecutive sum 

# N = (x + 1) + ... + (x + k)
# N = x k + k(k + 1)/2

def consecutiveNumbersSum(self, N: int) -> int:
    count = 0
    # x > 0 --> N/k - (k + 1)/2 > 0
    upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
    for k in range(1, upper_limit):
        # x should be integer
        if (N - k * (k + 1) // 2) % k == 0:
            count += 1
    return count