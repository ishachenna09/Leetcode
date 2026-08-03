class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<=j and j>=0:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            else :
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i+=1
                    j-=1     
        
        return True                 
        # ns=""
        # for i in s :
        #     if i.isalnum():
        #         ns+=i.lower()
        # i=0
        # j=len(ns)-1
        # print(ns)
        # while i<=j and j>=0:
        #     print(i,j)
        #     if ns[i]!=ns[j]:
        #         return False
        #     else:
        #         i+=1
        #         j-=1
        # return True                
                     
