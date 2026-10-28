# SOLUTION - 1
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        W = max(nums)
        nums.remove(W)
        X = max(nums)

        Y = min(nums)
        nums.remove(Y)
        Z = min(nums)

        return (W*X) - (Y*Z)

# SOLUTION - 2
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])