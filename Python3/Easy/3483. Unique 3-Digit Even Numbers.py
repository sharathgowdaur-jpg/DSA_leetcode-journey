class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        for i,j,k in permutations(digits,3):
            if i != 0 and k % 2 == 0:
                numbers.add((i,j,k))
        return len(numbers)