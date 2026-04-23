class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) 
        bucket = [[] for i in range(n+1)]
        freq = defaultdict(int) 
        for number in nums:
            freq[number] += 1 
        
        for num, occur in freq.items():
            bucket[occur].append(num)
        
        res = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res