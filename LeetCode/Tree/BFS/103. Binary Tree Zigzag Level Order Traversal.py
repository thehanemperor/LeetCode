class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        lev = 0
        queue = deque([root])
        result = []
        while queue:
            tmp = deque([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not lev%2:
                    tmp.append(curr.val)
                else:
                    tmp.appendleft(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append([*tmp])
            lev += 1
            
        return result