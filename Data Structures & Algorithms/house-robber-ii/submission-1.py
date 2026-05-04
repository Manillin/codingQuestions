class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(houses):
            prev2 = 0
            prev1 = 0
            for num in houses:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current 
            return prev1
        
        exclude_last = rob_line(nums[:-1])
        exclude_first = rob_line(nums[1:])

        return max(exclude_last, exclude_first)
