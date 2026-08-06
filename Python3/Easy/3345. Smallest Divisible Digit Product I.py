class Solution:
    def nproduct(self,n):
        product = 1
        while n != 0:
            product *= n % 10
            n = n//10
        return product
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            ans = self.nproduct(n)
            if ans % t == 0:
                return n
            else:
                n += 1