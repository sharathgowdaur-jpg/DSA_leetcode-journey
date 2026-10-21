# SOLUTION - 1:
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for ch in s:
            if 65 <= ord(ch) <= 90:
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result


# SOLUTION - 2:
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()