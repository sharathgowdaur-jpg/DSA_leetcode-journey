# SOLUTION - 1
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        box=1
        while box <= n:
            n-=box
            count+=1
            box+=1
        return count


# SOLUTION - 2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        high=n
        low=1
        while low<=high:
            mid=(low+high)//2
            sum_mid=(mid*(mid+1))//2
            if sum_mid==n:
                return mid
            elif sum_mid>n:
                high=mid-1
            else:
                low=mid+1
        return high