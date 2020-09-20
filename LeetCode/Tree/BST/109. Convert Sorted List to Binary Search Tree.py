class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        def findMid(head,end):
            slow,fast = head,head
            while fast!=end and fast.next!=end:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def dfs(node,start,end):
            if start == end:
                return None
            
            mid = findMid(start,end)
            root = TreeNode(mid.val)
            root.left = dfs(node,start,mid)
            root.right = dfs(node,mid.next,end)
            return root
        
        return dfs(head,head,None)