class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nMap = {}
        for num in nums:
            if num in nMap:
                return True 
            else:
                nMap[num] = 1
        return False 
