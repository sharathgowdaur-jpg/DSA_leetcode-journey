class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_sum = sum(nums[:k])

        max_sum = sum(nums[-k:])

        return max_sum - min_sum