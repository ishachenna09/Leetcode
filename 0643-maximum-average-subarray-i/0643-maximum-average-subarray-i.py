class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        csum = 0
        avg = float('-inf')
        for i in range(len(nums)):
            csum += nums[i] 
            if i >= k-1 :
                cavg = csum /k 
                avg = max(avg,cavg)
                csum -= nums[i-k+1]
        return avg         
        