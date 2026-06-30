#solution 1
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign=1
        for num in nums:
            if num==0:
                return 0
            elif num < 0:
                sign=-sign
        return sign
    
#solution2
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if num==0:
                return 0
            elif num < 0:
                count+=1
        if count%2==0:
            return 1
        else:
            return -1