# SOLUTION - 1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=1
        high=num
        while low<=high:
            number=(low+high)//2
            answer=number*number
            if answer==num:
                return True
            elif answer<num:
                low=number+1
            else:
                high=number-1
        return False


    #SOLUTION - 2
    class Solution:
        def isPerfectSquare(self, num: int) -> bool:
            i=1
            while True:
                res=i*i
                i+=1
                if res==num:
                    return True
                elif res > num:
                    return False
