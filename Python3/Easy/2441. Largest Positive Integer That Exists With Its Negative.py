class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        res = -1
        array = set(nums)

        for num in nums:
            if num > res and -num in array:
                res = num
        return res