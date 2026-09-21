class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = freq = [0] * k

        for num in nums:
            num %= k
            cur = [0] * k
            cur[num] = 1

            for x,y in enumerate(freq):
                cur[x * num % k] += y

            freq = cur
            for x,y in enumerate(freq):
                res[x] += y
        return res