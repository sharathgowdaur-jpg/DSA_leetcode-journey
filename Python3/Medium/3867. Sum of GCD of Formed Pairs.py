class Solution:
    def gcd(self,a,b):
        while b!=0:
            temp=a
            a=b
            b=temp%b
        return a
    def gcdSum(self, nums: list[int]) -> int:
        prefgcd=[0]*len(nums)
        maximum=-1

        for i in range(len(nums)):
            maximum=max(maximum,nums[i])
            prefgcd[i] = self.gcd(maximum,nums[i])
        
        prefgcd.sort()
        total=0
        i=0
        j=len(prefgcd)-1
        while i<j:
            total+=self.gcd(prefgcd[i],prefgcd[j])
            i+=1
            j-=1
        return total