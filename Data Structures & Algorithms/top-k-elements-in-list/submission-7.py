class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1 
        
        max_heap = []
        for num, occur in freq.items():
            heapq.heappush(max_heap, (-occur, num))
        res = []
        for i in range(k):
            occur, num = heapq.heappop(max_heap)
            res.append(num)
        return res
        
        