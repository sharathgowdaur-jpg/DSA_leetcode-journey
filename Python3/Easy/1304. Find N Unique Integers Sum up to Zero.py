class Solution:
    def sumZero(self, n: int) -> list[int]:
        return [n * (1 - n) // 2 ] + list(range(1,n))