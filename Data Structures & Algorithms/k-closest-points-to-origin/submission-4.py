class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = x**2  + y**2 
            heapq.heappush(heap, [-dist, x, y])
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for dist, x ,y in heap:
            res.append([x,y])
        return res

