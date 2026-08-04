# SOLUTION - 1
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        minimun = min(nums)
        maximum = max(nums)
        hashset = set(nums)
        missing = []
        for i in range(minimun,maximum+1):
            if i not in hashset:
                missing.append(i)
        return missing

# SOLUTION - 2
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        hashset = set(nums)
        missing = []
        for i in range(nums[0],nums[-1]):
            if i not in hashset:
                missing.append(i)
        return missing

# SOLUTION - 3
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []
        j = 0
        for i in range(nums[0],nums[-1]):
            if nums[j] != i:
                missing.append(i)
            else:
                j += 1
        return missing
