class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        prev = 1

        for i in range(1,rowIndex + 1):
            next_ans = prev * (rowIndex - i + 1) // i
            result.append(next_ans)
            prev = next_ans
        return result