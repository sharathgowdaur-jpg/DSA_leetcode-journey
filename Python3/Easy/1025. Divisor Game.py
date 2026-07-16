# SOLUTION - 1
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2 == 0:
            return True
        else:
            return False


# SOLUTION - 2
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n%2 == 0