class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = 0

        for num in numset:
            if num-1 not in numset:
                seq = 1
                while num + seq in numset:
                    seq+=1
                max_length = max(max_length, seq)
            else:
                continue 
        return max_length 