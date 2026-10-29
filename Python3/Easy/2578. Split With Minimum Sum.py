class Solution:
    def splitNum(self, num: int) -> int:
        My_list = []
        while num != 0:
            digit = num % 10
            num = num //  10
            My_list.append(digit)
        My_list.sort()
        num1 = 0
        num2 = 0
        for i in range(len(My_list)):
            if i % 2 == 0:
                num1 = num1 * 10 + My_list[i]
            else:
                num2 = num2 * 10 + My_list[i]

        return num1 + num2