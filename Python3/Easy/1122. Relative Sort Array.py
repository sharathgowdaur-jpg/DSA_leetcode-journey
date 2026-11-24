class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ans = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    ans.append(arr1[j])
                    arr1[j] = -1
        arr1.sort()
        for num in arr1:
            if num != -1:
                ans.append(num)
        return ans