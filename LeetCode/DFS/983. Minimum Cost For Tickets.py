# MEDIUM
# recursion 
#     1. set a range with 365
#         recursion can not go beyond 365. each recursive call, we check if the day exists in schedule,
#         if yes: check three jumps index + (1,7,30) 

#         Time O(365) Space O(365)
    
#     2. recursion in schedule range:
#         instead jumps (1,7,30), we jump to next index 

    

def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        mem = [0]*n
        trav = set(days)
        durations = [1,7,30]
        def dfs(index):
            if index>365:
                return 0
            if mem[index]:
                return mem[index]
            
            if index in trav:
                result = min(dfs(index+1)+costs[0], dfs(index+7)+costs[1],\
                             dfs(index+30)+costs[2])
            else:
                result = dfs(index+1)
                
            mem[index] = result 
            return result
        
        def fasterDFS(index):
            if index >= n:
                return 0
            if mem[index]:
                return mem[index]
            
            j = index
            result = float("inf")
            for k in range(3):
                while j< n and days[j] < days[index] +durations[k]:
                    #print('j',j,'i+',durations[k],"=",days[index] +durations[k])
                    j += 1
                result = min(result,fasterDFS(j)+ costs[k]) 
                #print('index',index,"=",result,'k',durations[k])
            mem[index] = result
            return result
        
        return fasterDFS(0)