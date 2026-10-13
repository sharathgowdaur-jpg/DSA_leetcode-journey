class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        ans = n // 2
        mins = nums[:ans]
        maxs = nums[ans:]
        return sum(maxs) - sum(mins)