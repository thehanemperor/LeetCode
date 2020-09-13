# EASY 
# set all non prime numbers to 0 from 2 => 2*i 

# Time O(N) Space O(N)

class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [1]*n
        
        for i in range(2,int(n**0.5)+1):
            j = 2
            while nums[i] and i*j < n:
                nums[i*j] = 0
                j += 1
                
        # count = 0
        # for i in range(2,n):
        #     if nums[i]:
        #         count +=1
                
        return sum(nums[2:])