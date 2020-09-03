# HARD
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        appear = set([])
        stack = []
        lastOccur = {s[i]:i for i in range(len(s))}
        print(lastOccur)
        for i,c in enumerate(s):
            # check if we have it in stack using set
            if c not in appear:
                # if current char has lower value and there is one more stack[-1] 
                # at the following string, then we have to pop the previous one
                while stack and c< stack[-1] and i < lastOccur[stack[-1]]:
                    appear.remove(stack.pop())
                    
                appear.add(c)
                stack.append(c)
        return ''.join(stack)
        print(stack)
        