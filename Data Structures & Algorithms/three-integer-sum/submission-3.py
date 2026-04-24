class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)-2, 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l = i+1
            r = len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
                     