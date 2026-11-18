class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS= {}
        countT= {}         
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0)+1
            countT[t[i]] = countT.get(t[i],0)+1  
        return countS == countT
        # if len(s) == len(t):
        #     if sorted(s) == sorted(t):
        #         return True
        # return False         
   