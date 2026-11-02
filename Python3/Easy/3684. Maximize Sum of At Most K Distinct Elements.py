class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        hashset = set()
        output = []
        nums.sort(reverse = True)
        for num in nums:
            elif num not in hashset and k > 0:
                hashset.add(num)
                output.append(num)
                k -= 1

        return output