# EASY
# same as find sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num< 2:
            return True
        a,b = 2,num//2
        while a <= b:
            mid = a+ (b-a)//2
            sqr = mid*mid
            if sqr == num:
                return True
            elif sqr < num:
                a = mid +1
            elif sqr > num:
                b = mid -1
                
        return False