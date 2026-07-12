class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array=sorted(arr)
        rank=1
        rank_holder={}
        for num in sorted_array:
            if num not in rank_holder:
                rank_holder[num]=rank
                rank+=1
        return [rank_holder[num] for num in arr]