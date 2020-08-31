# HARD
# record  count {nums[i]: appearTimes } 
#         freq {count[nums[i]]: appearTimes}

# ex => input = [2,2,1,1,5,3,3,5]
#         freq defaultdict(<class 'int'>, {1: 4, 2: 4})
#         count defaultdict(<class 'int'>, {2: 2, 1: 2, 5: 2, 3: 2})

# we start from the last index of input 
# check if count[nums[i]] * freq[count[nums[i]]] == i. this is to removed nums[i] itself

# check if count[nums[i-1]] * freq[count[nums[i-1]]] == i. this is to removed nums[i-1]



class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # freq,count = [0]*10001,[0]*10001
        freq,count = defaultdict(int),defaultdict(int)
        n = len(nums)
        for i in range(n):
            count[nums[i]]+= 1
            freq[count[nums[i]]] += 1
          
        print('freq',freq)
        print('count',count)
        
        for i in range(n-1,0,-1):
            print('count:{}, freq:{}, multi:{}'.format(count[nums[i]],freq[count[nums[i]]],i))
            if count[nums[i]] * freq[count[nums[i]]] == i:
                return i+1
            
            freq[count[nums[i]]] -=1
            count[nums[i]]-=1
            
            if count[nums[i-1]] * freq[count[nums[i-1]]] == i:
                return i +1
            
        return 1