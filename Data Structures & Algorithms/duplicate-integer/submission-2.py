class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = set(nums)
        return not len(nset) == len(nums)
