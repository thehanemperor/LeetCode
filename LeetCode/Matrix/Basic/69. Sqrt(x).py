class Solution:
    def mySqrt(self, x: int) -> int:
        if x< 2:
            return x
        left,right = 2, x//2

        while left <= right:
            mid = left + (right -left)//2
            num = mid ** 2
            print(mid,num)
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
            
        return right