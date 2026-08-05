class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hashset = set()
        x,y = 0,0
        hashset.add((x,y))
        for s in path:
            if s =="N":
                y+=1
            elif s =="S":
                y-=1
            elif s =="E":
                x+=1
            else:
                x-=1
            if (x,y) in hashset:
                return True
            hashset.add((x,y))
        return False