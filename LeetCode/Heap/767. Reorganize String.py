# MEDIUM
# Same as 358

from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, S: str) -> str:
        m = [0]*26 
        for c in S:
            m[ord(c)-ord("a")]+= 1
            
        heap = []
        for i,v in enumerate(m):
            if v > 0:
                heappush(heap,(-v,i))
        result = []
        while heap:
            tmp = []
            for i in range(2):
                curr = heappop(heap)
                result.append(chr(curr[1]+ord("a")))
                tmp.append(curr[1])
                if not heap:
                    if i != 1 and len(result)!= len(S):
                        return ""
                    break
                    
            for t in tmp:
                m[t]-=1
                if m[t]>0:
                    heappush(heap,(-m[t],t))
                    
        return "".join(result)