class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore algorith
        count =0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
                count =1
            elif candidate == num:
                count+=1
            else:
                count-=1
        actualCount = nums.count(candidate)
        if actualCount > len(nums)//2:
            return candidate
        else:
            return None                    


       
