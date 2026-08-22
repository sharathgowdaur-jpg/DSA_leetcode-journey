class Solution:
    def sum_product(self,n):
        sum1 = 0
        product = 1
        while n != 0:
            number = n % 10
            sum1 += number
            product *= number
            n = n // 10
        ans = sum1 + product
        return ans
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        res = self.sum_product(n)
        if temp % res ==0:
            return True
        else:
            return False