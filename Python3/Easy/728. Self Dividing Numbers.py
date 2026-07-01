class Solution:
    def check(self,n):
        num=n
        while(n!=0):
            r=n%10
            n=n//10
            if r==0:
                return False
            elif num%r!=0:
                return False
        return True
            
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            if self.check(i):
                ans.append(i)
        return ans