class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0]*(mx+1)
        for num in nums:
            freq[num]+=1

        gcd=[0]*(mx + 1)
        for i in range(mx,0,-1):
            sm = sum(freq[i::i])
            gcd[i] = sm * (sm-1)//2-sum(gcd[i::i])