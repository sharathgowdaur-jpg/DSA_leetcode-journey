class Solution:
    def countCommas(self, n: int) -> int:
        comma,p = 0,1000

        while p <= n:
            comma += n - p + 1
            p *= 1000
        return comma