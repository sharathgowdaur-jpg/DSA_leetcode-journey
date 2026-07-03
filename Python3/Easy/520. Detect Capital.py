class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=0
        for s in word:
            if s.isupper():
                count+=1
        if count==len(word):
            return True
        elif count==0:
            return True
        elif count==1 and word[0].isupper():
            return True
        else:
            return False