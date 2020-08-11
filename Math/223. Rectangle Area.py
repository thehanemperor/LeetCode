# MEDIUM 
# left + right - overlapped
# time O(1) space O(1)

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        left = max(A,E)
        right = max(min(C,G),left)
        bot = max(B,F)
        top = max(min(D,H),bot)
        
        return (C-A)*(D-B) - (right-left)*(top-bot) + (G-E)*(H-F)