# SOLUTION - 1
class Solution:
    def maxProduct(self, n: int) -> int:
        array = []
        while n!=0:
            r = n%10
            n = n//10
            array.append(r)
        array.sort()
        product = array[-1]*array[-2]
        return product

# SOLUTION - 2
class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = 0
        max2 = 0
        while n!=0:
            r = n % 10
            n = n//10
            if r > max1:
                max2 = max1
                max1 = r
            elif r > max2:
                max2 = r
        return max1 * max2