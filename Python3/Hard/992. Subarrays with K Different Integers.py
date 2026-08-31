class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k) - self.atMost(nums,k - 1)

    def atMost(self,nums,k):
        hashmap = {}
        left = 0
        count = 0

        for right in range(len(nums)):
            hashmap[nums[right]] = hashmap.get(nums[right],0) + 1

            while len(hashmap) > k:
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]]==0:
                    del hashmap[nums[left]]
                left += 1
            count += right - left + 1
        return count