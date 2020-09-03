# HARD 

# Heap 

# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"

# 1. find the frequency of each char in the input and store em in a heap 
#     ==>  a: 3, b:2, c:2, d: 1 

# 2. pop the heap till its empty 
#     ==>
#         while heap is not empty 
#             pop the heap k times.   since here k == 2, we popped  a,b 
#             store the popped value to result, and a tmp 

#             after k pops: 
#                 decrement each t-- in [tmp], 
#                 if the frequency of t is still >0, push it back 

# eg. => 
#     1st:    a: 3, b:2, c:2, d: 1 
#             a,b  
#     2nd:    a:2, c:2, b:1, d:1 
#             a,c 
#     3rd:    a:1, b:1, c:1, d:1 
#             a,b
#     4th:    c:1, d:1 
#             c,d  
#     result => a,b,a,c,a,b,c,d 


from heapq import heappush, heappop
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        m = [0]*26
        for c in s:
            m[ord(c)-ord("a")]+= 1
            
        heap =[]
        for i,v in enumerate(m):
            if v>0:
                heappush(heap,(-v,i))
        
        result = []
        print(heap)
        while heap:
            tmp = []
            for i in range(k):
                curr = heappop(heap)
                #print('heap',curr)
                result.append(chr(curr[1]+ord("a")))
                tmp.append(curr[1])
                if not heap:
                    #print(result)
                    if not i == k-1 and not len(result) == len(s):
                        return ""
                    break
            print('pop k times',tmp)
                    
            for t in tmp:
                m[t] -= 1
                if m[t]>0:
                    heappush(heap,(-m[t],t))
        
        return "".join(result)
        print(result)