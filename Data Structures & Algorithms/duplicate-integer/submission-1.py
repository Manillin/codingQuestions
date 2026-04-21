class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        return False if len(my_set) == len(nums) else True
        