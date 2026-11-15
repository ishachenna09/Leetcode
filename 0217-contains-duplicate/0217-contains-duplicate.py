class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        non_duplicate_len = len(set(nums))
        len_nums = len(nums)
        if  non_duplicate_len != len_nums :
            return True
        else:
            return False          
        