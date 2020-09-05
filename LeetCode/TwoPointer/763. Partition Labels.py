# MEDIUM 
# 1. find first/last occurence of each character
# 2. merge interval base on the [start,end] of each character
# Time O(n)  Space O(1)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        first = [-1]*26
        last = [-1]*26
        for i,v in enumerate(S):
            if first[ord(v)- ord("a")]== -1:
                first[ord(v)- ord("a")] = i
            last[ord(v)-ord("a")] = i
            
        #print(first)
        #print(last)
        interval = [list(a) for a in filter(lambda x:x[0]!=-1,zip(first,last))]
        
        interval.sort(key= lambda x:x[0])
        #print(interval)
        slow,fast = 0,1
        while fast <len(interval):
            if interval[fast][0]<= interval[slow][1]:
                if interval[fast][1]> interval[slow][1]:
                    interval[slow][1]=interval[fast][1]
            else:
                slow += 1
                interval[slow] = [*interval[fast]]
            fast += 1
        return [ j-i+1 for i,j in interval[:slow+1]]
        print(interval[:slow+1])