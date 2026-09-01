class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = 0 
        missing = 0
        hashset = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in hashset:
                    repeated = grid[i][j]
                else:
                    hashset.add(grid[i][j])
        n = len(grid)
        length = n*n
        for m in range(1,length+1):
            if m not in hashset:
                missing = m
        return [repeated,missing]