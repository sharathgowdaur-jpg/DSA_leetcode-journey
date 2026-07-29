class Solution:
    def smallestPalindrome(self, s: str) -> str:
        divide = len(s) // 2
        first_half = sorted(s[:divide])
        mid = [s[divide]] if len(s) % 2 == 1 else []
        last_half = first_half[::-1]
        return "".join(first_half + mid + last_half)
