class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        if len(words) <=1:
            return words
        i=1    
        while i<len(words):
            sort1 = "".join(sorted(words[i]))
            sort2 = "".join(sorted(words[i-1]))
            if sort1 == sort2:
                words.remove(words[i])  
            else:
                i+=1
        return words        

        