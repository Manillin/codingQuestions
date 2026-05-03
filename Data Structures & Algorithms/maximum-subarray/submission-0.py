class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalSum = nums[0]
        localSum = 0
        for num in nums:
            localSum += num 
            totalSum = max(totalSum, localSum)
            if localSum < 0:
                localSum = 0
            
        return totalSum 