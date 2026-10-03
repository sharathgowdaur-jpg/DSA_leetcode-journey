class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def Backtrack(start,path):
            result.append(path)
            for i in range(start,len(nums)):
                Backtrack(i+1,path + [nums[i]])

        Backtrack(0,[])
        return result
