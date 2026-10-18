class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        word_s1 = s1.split()
        word_s2 = s2.split()

        all_word = word_s1 + word_s2

        word_count = Counter(all_word)

        return [word for word in word_count if word_count[word] == 1]