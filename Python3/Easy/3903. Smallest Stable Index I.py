class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix = [0] * n
        suffix[n - 1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])

        maximum = 0

        for i, x in enumerate(nums):
            maximum = max(maximum, x)

            if maximum - suffix[i] <= k:
                return i

        return -1