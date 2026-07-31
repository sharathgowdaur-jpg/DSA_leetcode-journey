# SOLUTION - 1
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)


# SOLUTION - 2
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types_candy = set(candyType)
        n = len(candyType)//2
        if len(types_candy) >= n:
            return n
        else:
            return len(types_candy)