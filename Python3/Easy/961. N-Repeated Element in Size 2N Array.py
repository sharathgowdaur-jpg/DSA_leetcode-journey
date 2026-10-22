class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        repeat = set()
        for num in nums:
            if num not in repeat:
                repeat.add(num)
            else:
                return num