class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0
        for i,alpha in enumerate(s):
            alphabet = 26 - (ord(alpha) - ord('a'))
            position = i + 1

            answer += position * alphabet
        return answer