class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        Total = 1
        i=2
        while i * i <= num:
            if num % i == 0:
                Total += i
                if i * i != num:
                    Total += num // i
            i += 1

        return Total == num