MEDIUM
bucket sort 

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        check = {}
        if t<0:
            return False
        for i in range(len(nums)):
            bucket = nums[i] // (t+1)
            for j in [-1,0,1]:
                if bucket +j in check and abs(nums[i]-check[bucket+j])<=t:
                    return True
            check[bucket] = nums[i]
            if i >=k:
                check.pop(nums[i-k]//(t+1))
        
            
        return False