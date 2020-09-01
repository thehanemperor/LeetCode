# MEDIUM 

# Recursively find & delete the node because we want to reassign the parent node
#  eg. root.left = deleteNode(root.left)

# 1. if the node being deleted is leaf, just set it to None and return to parent

# 2. not leaf but have right child, find the first larger node than root. ==> root.right, root.left.... 

# 3. not leaf, do not have right child but have left child, take the largest smaller node of root ==> root.left, root.right .... 

# Time O(H)  Space O(H)

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key> root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            print(root.val,root.left,root.right)
            if not root.left and not root.right:
                print("its a leaf")
                root = None
            elif root.right:
                print("not leaf,and have right")
                root.val = self.findFirstLarge(root.right)
                root.right = self.deleteNode(root.right,root.val)
            else:
                print("not leaf and have left")
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left,root.val)
            
        
        return root
    
    def findFirstLarge(self,root):
        while root.left:
            root = root.left
            
        return root.val
    
    
    def predecessor(self,root):
        while root.right:
            root = root.right
            
        return root.val
    
    