#SOLUTION - 1
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        sumx = 0
        for i in range(0,n,2):
            sumx += nums[i]
        return sumx

#SOLUTION - 2
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse =True)
        sumx = 0
        for i in range(1,len(nums),2):
            sumx += nums[i]
        return sumx

#SOLUTION - 3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)-2
        sumx = 0
        for i in range(n,-1,-2):
            sumx += nums[i]
        return sumx