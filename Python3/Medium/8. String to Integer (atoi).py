class Solution:
    def string_to_num(self,num):
        digits = {
            '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,
            '6':6,'7':7,'8':8,'9':9
        }
        sign = 1
        i = 0
        answer = 0
        if num[0]=="-":
            sign = -1
            i = 1
        elif num[0]=="+":
            sign = 1
            i=1
        while i < len(num):
            answer = answer*10 + digits[num[i]]
            i+=1
        return sign * answer
    def myAtoi(self, s: str) -> int:
        num = ""
        for i in range(len(s)):
            if s[i] == " " and len(num)==0:
                continue
            elif (s[i]=="-" or s[i]=="+") and len(num)==0:
                num += s[i]
            elif s[i].isdigit():
                num+=s[i]
            else:
                break
        if num =="" or num =="-" or num =="+":
            return 0
        ans = self.string_to_num(num)
        if ans < -2**31:
            return -2**31
        if ans > 2**31 - 1:
            return 2**31 - 1
        return ans