# HARD
# build 2 stacks store successor and predecssor with O(H) time 
# merge 2 stack with O(K) time 

# Time: O(H)

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def initSucc(root,tar):
            large = []
            while root:
                if root.val == tar:
                    large.append(root)
                    break
                elif root.val > tar:
                    large.append(root)
                    root = root.left 
                else :
                    root = root.right 
                    
            return large
        
        def initPrev(root,tar):
            arr = []
            while root:
                if root.val == tar:
                    arr.append(root)
                    break
                    
                elif root.val < tar:
                    arr.append(root)
                    root = root.right
                else:
                    root = root.left 
                    
            return arr
        
        def getNextPrev(prev):
            curr = prev.pop()
            ret = curr.val
            curr = curr.left
            while curr:
                prev.append(curr)
                curr = curr.right
            return ret
        
        def getNextSucc(succ):
            curr = succ.pop()
            ret = curr.val 
            curr = curr.right 
            
            while curr:
                succ.append(curr)
                curr = curr.left 
                
            return ret
                    
        
        succ,prev = initSucc(root,target),initPrev(root,target)
        print([r.val for r in prev])
        print([r.val for r in succ])
        if succ and prev and succ[-1].val == prev[-1].val:
            getNextPrev(prev)
            
        print([r.val for r in prev])
        print([r.val for r in succ])
        
        ret = []
        while k >0 :
            if not succ:
                ret.append(getNextPrev(prev)) 
            elif not prev:
                ret.append(getNextSucc(succ))
            else:
                succDiff = abs(succ[-1].val - target)
                prevDiff = abs(prev[-1].val -target)
                if succDiff < prevDiff:
                    ret.append(getNextSucc(succ))
                else:
                    ret.append(getNextPrev(prev))
            k-= 1
            
        return ret
        
        
        