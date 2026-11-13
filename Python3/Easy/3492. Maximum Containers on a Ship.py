class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        e = n * n
        t = maxWeight//w
        return min(e,t)