class Solution:
    def checkString(self, s: str) -> bool:
        hashset = set()
        for i in s:
            if i == "a" and "b" in hashset:
                return False
            else:
                hashset.add(i)
        return True