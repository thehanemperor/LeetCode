# EASY 
# since we cannot use a helper array, we merge those two arrays from tails 
# input:
#         [1,2,3,0,0,0]
        
#         [2,5,6]

#         two pointer i,j start from arr1[2], arr2[2], and only merge the larger one

# time O(N)  space O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m+n -1
        i,j = m-1,n-1
        while i >=0 and j >=0:
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                i -=1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        
        while i>=0:
            nums1[index] = nums1[i]
            i-=1
            index -= 1
            
        while j >=0:
            nums1[index] = nums2[j]
            j-= 1
            index -=1