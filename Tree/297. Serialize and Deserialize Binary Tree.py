# HARD 
# Tree: 
#                         1                       
#                     /       \
#                    2          3                 =>    [1,2,3,4,None,5,6,None, None,None,None,None]
#                 /    \      /    \
#               4      None  5      None 

# Time O(N) Space O(N)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            
            curr = queue.popleft()
            result.append(curr.val) if curr else result.append(curr)
            if not curr:
                
                continue
            queue.append(curr.left)
            queue.append(curr.right)
        
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        index = 1
        root = TreeNode(data[0])
        queue = deque([root])
        
        while queue and index< len(data):
            curr = queue.popleft()
            if data[index]!= None:
                curr.left = TreeNode(data[index])
                queue.append(curr.left)
            
            index += 1
            if data[index]!= None:
                curr.right = TreeNode(data[index])
                queue.append(curr.right)
            index += 1
            
        return root
        