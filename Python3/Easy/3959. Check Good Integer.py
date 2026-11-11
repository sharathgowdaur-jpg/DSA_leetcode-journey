class Solution:
    def digit(self,num):
        digitSum = 0
        squareSum = 0
        while num != 0:
            s = num % 10
            digitSum += s
            squareSum += s * s
            num = num//10
        return digitSum,squareSum
    def checkGoodInteger(self, n: int) -> bool:
        digitSum,squareSum = self.digit(n)
        if squareSum - digitSum >= 50:
            return True
        else:
            return False