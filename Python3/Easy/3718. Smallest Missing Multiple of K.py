# SOLUTION - 1
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num = set(nums)
        i = 1
        ans = i * k
        while True:
            if ans in num:
                i += 1
                ans = i * k
            else:
                return ans

# SOLUTION - 2
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num = set(nums)
        i = 1
        ans = i * k
        while True:
            if ans not in num:
                return ans
            else:
                i += 1
                ans = i * k