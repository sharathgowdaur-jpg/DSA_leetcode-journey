# SOLUTION = 1:
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        ans = []
        for word in words:
            lower = set(word.lower())

            for row in rows:

                if lower <= row:
                    ans.append(word)
        return ans

#SOLUTION 2:
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []
        for word in words:
            lower = set(word.lower())

            if lower <= row1 or lower <= row2 or lower <= row3:
                ans.append(word)
        return ans


#SOLUTION 3:
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []
        for word in words:
            lower = word.lower()
            if all(c in row1 for c in lower):
                ans.append(word)
            elif all(c in row2 for c in lower):
                ans.append(word)
            elif all(c in row3 for c in lower):
                ans.append(word)
        return ans