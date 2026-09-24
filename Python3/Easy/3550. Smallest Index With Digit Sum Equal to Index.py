class Solution:
    def sumofdigit(self, number):
        if number <= 9:
            return number
        digit = 0
        while number != 0:
            num = number % 10
            digit += num
            number = number // 10
        return digit

    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ans = self.sumofdigit(nums[i])
            if ans == i:
                return i
        return -1