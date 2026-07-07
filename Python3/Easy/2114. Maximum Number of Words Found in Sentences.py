#SOLUTION==1
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word=0
        for s in sentences:
            max_word=max(max_word,len(s.split(" ")))
        return max_word

#SOLUTION==2
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word=0
        for s in sentences:
            word=1
            for i in s:
                if i==" ":
                    word+=1
            max_word=max(max_word,word)
        return max_word