class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if set(s) != set(goal):
            return False
        return goal in s + s