class Solution:
    def minimumSum(self, num: int) -> int:
        string = str(num)
        array = []
        for s in string:
            array.append(int(s))
        array.sort()
        n = len(array)//2
        new1 = array[:n]
        new2 = array[n:]
        digit1 = (new1[0] * 10) + new2[0]
        digit2 = (new1[1] * 10) + new2[1]
        result = digit1 + digit2
        return result