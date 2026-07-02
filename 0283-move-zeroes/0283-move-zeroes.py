class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0, 0
        while i < len(n) and j<len(n):
            if n[i] !=0:
                n[i],n[j] = n[j],n[i]
                j+=1
            i+=1    
        
            

           