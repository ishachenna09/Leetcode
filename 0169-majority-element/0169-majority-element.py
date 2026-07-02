class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            counts[i] =counts.get(i,0)+1
        for k,v in counts.items():
            if v > (len(nums))//2:
                return k
