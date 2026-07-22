#SOLUTION - 1
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mix = list(zip(heights, names))
        mix.sort(reverse = True)

        return [name for height , name in mix]

#SOLUTION - 2
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        copy = heights.copy()
        copy.sort(reverse = True)

        used = set()
        output = []

        for h in copy:
            for i in range(len(heights)):
                if heights[i]==h and i not in used:
                    output.append(names[i])
                    used.add(i)
        return output