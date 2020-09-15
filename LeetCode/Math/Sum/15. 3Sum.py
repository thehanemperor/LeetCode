# Medium 
# for loop with twoSum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            tmp = self.twoSum(nums,i+1,0-nums[i])
            for t in tmp:
                merge = [nums[i]] + [*t]
                result.append([*merge])
                
        return result
                
    def twoSum(self,nums,index,tar):
        check = set([])
        appear = set([])
        result = []
        for i in range(index,len(nums)):
           
            if tar - nums[i] in check:
                if (tar-nums[i],nums[i]) not in appear:
                    result.append( [tar-nums[i],nums[i]] )
                appear.add((tar-nums[i],nums[i]))
                
            check.add(nums[i])
        #print('2sum',result)
        return result