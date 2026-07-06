class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        num=1
        while True:
            num*=4
            if num==n:
                return True
            elif num > n:
                return False
        