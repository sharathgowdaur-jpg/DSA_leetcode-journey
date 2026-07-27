# SOLUTION - 1
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for i in range(len(arr)):
            if target[i]!=arr[i]:
                return False
        return True


# SOLUTION - 2
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target)==sorted(arr)