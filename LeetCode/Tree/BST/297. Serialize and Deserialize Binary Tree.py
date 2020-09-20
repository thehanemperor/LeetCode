class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return ""
        queue = deque([root])
        result = []
        while queue:
            curr = queue.popleft()
            if curr:
                result.append(str(curr.val)) 
            else:
                result.append("null")
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
        
        print('ser','$'.join(result)  )
        return '$'.join(result) 
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print('data',data)
        if not data:
            return None
        index = 1
        nums = deque(data.split("$"))
        root = TreeNode(nums[0])
        queue = deque([root])
        
        while queue and index < len(nums):
            curr = queue.popleft()
            if nums[index] != "null":
                curr.left = TreeNode(nums[index])
                queue.append(curr.left)
            index += 1
            if nums[index]!= "null":
                curr.right = TreeNode(nums[index])
                queue.append(curr.right)
            
            index += 1
            
        return root