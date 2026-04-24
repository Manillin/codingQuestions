class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 

        while l < r: 
            l_sum = numbers[l] + numbers[r]
            if l_sum > target:
                r-=1
            elif l_sum < target:
                l+=1
            else:
                return [l+1, r+1]             
        