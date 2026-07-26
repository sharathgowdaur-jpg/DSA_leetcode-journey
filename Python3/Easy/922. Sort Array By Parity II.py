class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        ans = []
        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans