#SOLUTION==1
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3==0:
            n=n//3
        return  n==1
    

#SOLUTION==2
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        power=1
        while True:
            power*=3
            if power==n:
                return True
            elif power > n:
                return False
