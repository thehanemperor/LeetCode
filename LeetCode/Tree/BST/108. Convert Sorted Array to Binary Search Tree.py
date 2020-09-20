class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        return self.withoutRoot(nums,0,len(nums)-1)
        if not nums:
            return None
        
        root = TreeNode(0)
        self.dfs(nums,0,len(nums)-1,root)
        return root
    
    def withoutRoot(self,nums,left,right):
        if left > right:
            return None
        mid = left + (right - left >>1)
        root = TreeNode(nums[mid])
        root.left = self.withoutRoot(nums,left,mid-1)
        root.right = self.withoutRoot(nums,mid+1,right)
        return root
    
    def dfs(self,nums,left,right,root):
        if left > right:
            return
        mid = left + (right - left >>1)
        root.val = nums[mid]
        if left<= mid - 1:
            root.left = TreeNode()
        if mid+1<= right:
            root.right = TreeNode()
        print(nums[mid])
        
        self.dfs(nums,left,mid-1,root.left)
        self.dfs(nums,mid+1,right,root.right)