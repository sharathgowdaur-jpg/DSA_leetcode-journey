class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        ans = ""
        for key, value in sorted(hashmap.items(), key=lambda x: x[1], reverse=True):
            ans += key * value

        return ans