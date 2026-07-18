# SOLUTION - 1
class Solution:
    def gcd(a,b):
        while b!=0:
            temp=a
            a=b
            b=temp % b

    def findGCD(self, nums: List[int]) -> int:
        largest=0
        smallest=float('inf')
        for num in nums:
            largest = max(largest,num)
            smallest = min(smallest,num)
        return gcd(largest,smallest)


# SOLUTION - 2

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        largest=nums[-1]
        smallest=nums[0]
        return math.gcd(largest,smallest)