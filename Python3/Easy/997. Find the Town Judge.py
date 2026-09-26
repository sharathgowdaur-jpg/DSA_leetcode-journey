class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        COUNT = [0] * (n+1)

        for i,j in trust:
            COUNT[i] -= 1
            COUNT[j] += 1
        for i in range(1,n+1):
            if COUNT[i] == n-1:
                return i
        return -1