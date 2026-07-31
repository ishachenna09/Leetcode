class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for fast in range (slow, len(nums)):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow+=1
        return slow        
       
        