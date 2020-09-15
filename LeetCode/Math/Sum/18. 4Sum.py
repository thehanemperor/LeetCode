class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        result =[]
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            # print('4sum',nums[i],target- nums[i])
            tmp = self.threeSum(i+1,nums,target- nums[i])
            # print(tmp)
            for t in tmp:
                result.append([nums[i],t[0],t[1],t[2]])
            
        return result
        
        
    def threeSum(self,index, nums: List[int],tar) -> List[List[int]]:
        nums.sort()
        appear= set([])
        result = []
        for i in range(index,len(nums)):
            #print('3sum',nums[i],tar- nums[i])
            tmp = self.twoSum(nums,i+1,tar-nums[i])
            for t in tmp:
                if (nums[i],t[0],t[1]) not in appear:
                    merge = [nums[i]] + [*t]
                    result.append([*merge])
                appear.add((nums[i],t[0],t[1]))
                
        return result
                
    def twoSum(self,nums,index,tar):
        # print('twoSum',nums[index:])
        left,right = index,len(nums)-1 
        appear = set([])
        result = []
        while left < right:
            if nums[left] + nums[right] == tar:
                # print("2sum found",)
                if (nums[left], nums[right]) not in appear:
                    result.append([nums[left], nums[right]])
                    
                appear.add((nums[left], nums[right]))
                left += 1
                
            elif nums[left] + nums[right] < tar:
                left += 1
            elif nums[left] + nums[right] > tar:
                right -= 1
        
        
        # print('2sum',result)
        return result