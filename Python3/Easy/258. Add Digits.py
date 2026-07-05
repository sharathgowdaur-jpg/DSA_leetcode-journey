class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        while num:
            sum+=(num%10)
            num=num//10
            
        if sum<10:
            return sum
        else:
            return self.addDigits(sum)



class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        elif num % 9 ==0:
            return 9
        else:
            return num % 9