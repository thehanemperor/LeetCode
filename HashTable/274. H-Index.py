# MEDIUM 
# brute force:  
#     sort in decending order and check if a[i] > i 
#                 i       0	    1	    2	    3	    4	    5	    6
#     sorted citations	10	    9	    5	    3	    3	    2	    1
#     citations[i] > i	true	true	true	false	false	false	false

# Time O(NlogN) Space O(N)

# optimized: 
#         k	    0	1	2	3	4	5
#         count	0	1	1	2	0	1
#         s_k     5	5	4	3	1	1

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0 for _ in range(n+1)]
        for c in citations:
            papers[min(n,c)]+=1
        print(papers)
        k = n 
        s = papers[n]
        while k>s:
            k-=1
            s+=papers[k]
        
        return k